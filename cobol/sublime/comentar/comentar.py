import sublime, sublime_plugin

class ComentarCommand(sublime_plugin.WindowCommand):

	def run(self, automatic = True):
		settings = self.window.active_view().settings()

		if settings.get("txtComment"):
			self.setRows(settings.get("txtComment"))
		else:
			self.window.show_input_panel(
				'Qual o texto a ser comentado',
				'',
				self.setRows,
				None,
				None
			)

	def setRows(self, args):
		view = self.window.active_view()
		settings = view.settings()

		allcontent = sublime.Region(0, view.size())
		rows = view.split_by_newlines(allcontent)			
		row = view.line(view.sel()[0])
		nRow = 1

		for reg in rows:
			if(reg.begin() == row.begin()):
				break
			nRow += 1

		print(nRow)

		rStart = rEnd = nRow
		text = args[:6].upper() #O comentario só pode ter 6 caracteres

		settings.set("txtComment", text)

		if view:
			view.run_command(
				"insere_comentario",
				{"rStart": rStart, "rEnd": rEnd, "text": text}
			)

class ComentarLinhasCommand(sublime_plugin.WindowCommand):
	def run(self, automatic = True):
		view = self.window.active_view()
		settings = self.window.active_view().settings()

		if settings.get("txtComment"):		
			if len(view.sel()) > 1:
				view.run_command(
					"insere_comentario_na_region",
					{"text": settings.get("txtComment")}
				)
			else:
				self.window.show_input_panel(
					'Coloque a linha inicial e final. Ex: 1 10',
					'',
					self.loadCommentAndDo,
					None,
					None
				)
		else:
			if len(view.sel()) > 1:
				self.window.show_input_panel(
					'Qual o texto a ser comentado',
					'',
					self.saveCommentAndDo,
					None,
					None
				)
			else:
				self.window.show_input_panel(
					'Coloque a linha inicial e final e o texto. Ex: 1 10 XXXXXX',
					'',
					self.saveCommentAndDo,
					None,
					None
				)

	def loadCommentAndDo(self, args):
		settings = self.window.active_view().settings()

		(rStart, rEnd) = map(str, args.split(" "))

		text = settings.get("txtComment")

		self.setRows(rStart, rEnd, text)

	def saveCommentAndDo(self, args):
		settings = self.window.active_view().settings()

		try:
			(rStart, rEnd, text) = map(str, args.split(" "))
			text = text[:6].upper()
		except:
			text = args[:6].upper()
			rStart = 0
			rEnd = 0
			
		settings.set("txtComment", text)

		self.setRows(rStart, rEnd, text)

	def setRows(self, rStart, rEnd, text):
		if rStart == 0 and rEnd == 0:
			self.window.active_view().run_command(
				"insere_comentario_na_region",
				{"text": text}
			)
		else:
			self.window.active_view().run_command(
				"insere_comentario",
				{"rStart": rStart, "rEnd": rEnd, "text": text}
			)

class InsereComentarioCommand(sublime_plugin.TextCommand):
	def run(self, edit, rStart, rEnd, text):
		allcontent = sublime.Region(0, self.view.size())
		rows = self.view.split_by_newlines(allcontent)

		for i in range(int(rStart)-1, int(rEnd)):
			reg = sublime.Region(rows[i].begin(), rows[i].begin()+len(text))
			if(rows[i].size() < len(text)):
				self.view.insert(edit, rows[i].begin(), "." * (len(text) - rows[i].size()))
				allcontent = sublime.Region(0, self.view.size())
				rows = self.view.split_by_newlines(allcontent)
				reg = sublime.Region(rows[i].begin(), rows[i].begin()+len(text))

			
			self.view.replace(edit, reg, text)

class InsereComentarioNaRegionCommand(sublime_plugin.TextCommand):
	def run(self, edit, text):
		for i in self.view.sel():
			row = self.view.line(i)
			reg = sublime.Region(row.begin(), row.begin()+len(text))

			if(row.size() < len(text)):
				self.view.insert(edit, row.begin(), "." * (len(text) - row.size()))			

			self.view.replace(edit, reg, text)

class MudarTextoComentarioCommand(sublime_plugin.WindowCommand):
	def run(self, automatic = True):
		self.window.show_input_panel(
			'Qual o novo texto a ser comentado',
			'',
			self.changeText,
			None,
			None
		)

	def changeText(self, args):
		settings = self.window.active_view().settings()
		settings.set("txtComment", args)		