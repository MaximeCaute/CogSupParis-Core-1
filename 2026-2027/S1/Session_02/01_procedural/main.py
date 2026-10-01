import expyriment as xpy


xpy.control.set_develop_mode()

exp = xpy.design.Experiment(
    name="Ternus demonstration",
    background_colour=(0, 0, 0),
    foreground_colour=(255, 255, 255),
)
xpy.control.initialize(exp)

frame_a = xpy.stimuli.Canvas(size=(600, 300), colour=(0, 0, 0))
for x in (-120, -40, 40):
    xpy.stimuli.Circle(
        radius=20,
        position=(x, 0),
        colour=(255, 255, 255),
    ).plot(frame_a)

frame_b = xpy.stimuli.Canvas(size=(600, 300), colour=(0, 0, 0))
for x in (-40, 40, 120):
    xpy.stimuli.Circle(
        radius=20,
        position=(x, 0),
        colour=(255, 255, 255),
    ).plot(frame_b)

instructions = xpy.stimuli.TextScreen(
    heading="Ternus demonstration",
    text="Press SPACE to start.",
)

frame_a.preload()
frame_b.preload()
instructions.preload()

xpy.control.start(skip_ready_screen=True)

instructions.present()
exp.keyboard.wait(keys=[xpy.misc.constants.K_SPACE])

frame_a.present()
exp.clock.wait(250)
frame_b.present()
exp.clock.wait(700)

xpy.control.end()
