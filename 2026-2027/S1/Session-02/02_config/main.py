import expyriment as xpy

import config


xpy.control.set_develop_mode()

exp = xpy.design.Experiment(
    name=config.EXPERIMENT_NAME,
    background_colour=config.BACKGROUND,
    foreground_colour=config.FOREGROUND,
)
xpy.control.initialize(exp)

frame_a = xpy.stimuli.Canvas(
    size=config.CANVAS_SIZE,
    colour=config.BACKGROUND,
)
for x in config.FRAME_A_X:
    xpy.stimuli.Circle(
        radius=config.DOT_RADIUS,
        position=(x, 0),
        colour=config.FOREGROUND,
    ).plot(frame_a)

frame_b = xpy.stimuli.Canvas(
    size=config.CANVAS_SIZE,
    colour=config.BACKGROUND,
)
for x in config.FRAME_B_X:
    xpy.stimuli.Circle(
        radius=config.DOT_RADIUS,
        position=(x, 0),
        colour=config.FOREGROUND,
    ).plot(frame_b)

instructions = xpy.stimuli.TextScreen(
    heading="Ternus demonstration",
    text="Press SPACE to start.",
)

for stimulus in (frame_a, frame_b, instructions):
    stimulus.preload()

xpy.control.start(skip_ready_screen=True)

instructions.present()
exp.keyboard.wait(keys=[xpy.misc.constants.K_SPACE])

frame_a.present()
exp.clock.wait(config.FRAME_MS)
frame_b.present()
exp.clock.wait(700)

xpy.control.end()
