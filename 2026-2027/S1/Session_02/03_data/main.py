import expyriment as xpy

import config


xpy.control.set_develop_mode()

exp = xpy.design.Experiment(
    name=config.EXPERIMENT_NAME,
    background_colour=config.BACKGROUND,
    foreground_colour=config.FOREGROUND,
)

exp.data_variable_names = [
    "run_type",
    "transition",
    "frame_ms",
    "response",
    "key",
    "rt_ms",
]

xpy.control.initialize(exp)

frame_a = xpy.stimuli.Canvas(size=config.CANVAS_SIZE, colour=config.BACKGROUND)
for x in config.FRAME_A_X:
    xpy.stimuli.Circle(
        radius=config.DOT_RADIUS,
        position=(x, 0),
        colour=config.FOREGROUND,
    ).plot(frame_a)

frame_b = xpy.stimuli.Canvas(size=config.CANVAS_SIZE, colour=config.BACKGROUND)
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

response_screen = xpy.stimuli.TextScreen(
    heading="What did you see?",
    text="LEFT = element motion\nRIGHT = group motion",
)

for stimulus in (frame_a, frame_b,instructions, response_screen):
    stimulus.preload()

xpy.control.start(skip_ready_screen=True)

instructions.present()
exp.keyboard.wait(keys=[xpy.misc.constants.K_SPACE])

frame_a.present()
exp.clock.wait(config.FRAME_MS)
frame_b.present()
exp.clock.wait(config.FRAME_MS)

response_screen.present()
key, rt = exp.keyboard.wait(
    keys=[xpy.misc.constants.K_LEFT, xpy.misc.constants.K_RIGHT]
)

if key == xpy.misc.constants.K_LEFT:
    response = config.LEFT_KEY
else:
    response = config.RIGHT_KEY

exp.data.add(["self_test", "direct", config.FRAME_MS, response, key, rt])
exp.data.save()

xpy.control.end()
