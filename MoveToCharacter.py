import sublime, sublime_plugin

class MoveToCharacterCommand(sublime_plugin.TextCommand):
    def find_next(self, forward, char, before, pt):
        lr = self.view.line(pt)

        extra = 0 if before else 1

        if forward:
            line = self.view.substr(sublime.Region(pt, lr.b))
            idx = line.find(char, 1)
            if idx >= 0:
                return pt + idx + extra
        else:
            line = self.view.substr(sublime.Region(lr.a, pt))[::-1]
            idx = line.find(char, 0)
            if idx >= 0:
                return pt - idx - extra

        return pt

    def run(self, edit, character, extend = False, forward = True, before = True):
        current = self.view.sel()[0].begin()

        target = self.find_next(forward, character, before, current)

        if extend:
            self.view.sel().clear()
            self.view.sel().add(sublime.Region(current, target))
        else:
            self.view.sel().clear()
            self.view.sel().add(sublime.Region(target))

