class Light:
    def __init__(self): self.is_on = False
    def turn_on(self): self.is_on = True; print("Luz: ON")
    def turn_off(self): self.is_on = False; print("Luz: OFF")


class Command:
    def execute(self): raise NotImplementedError
    def undo(self): raise NotImplementedError


class TurnOnCommand(Command):
    def __init__(self, light): self.light = light
    def execute(self): self.light.turn_on()
    def undo(self): self.light.turn_off()


class TurnOffCommand(Command):
    def __init__(self, light): self.light = light
    def execute(self): self.light.turn_off()
    def undo(self): self.light.turn_on()


class RemoteControl:
    def __init__(self): self.history: list[Command] = []

    def press(self, command: Command):
        command.execute()
        self.history.append(command)

    def undo(self):
        if self.history:
            self.history.pop().undo()


light = Light()
remote = RemoteControl()
remote.press(TurnOnCommand(light))  # Luz: ON
remote.press(TurnOffCommand(light))  # Luz: OFF
remote.undo()  # Luz: ON
remote.undo()  # Luz: OFF
