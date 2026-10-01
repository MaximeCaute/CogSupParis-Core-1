import expyriment as xpy


xpy.control.set_develop_mode(True)
xpy.control.defaults.window_size = (800,800)
xpy.io.Keyboard.set_quit_key(xpy.misc.constants.K_ESCAPE)

start = (-250, 0)
end = (250, 0)
size = 20
white = (255,255,255)
cue_duration_ms = 200

experiment = xpy.design.Experiment(name="Illusory-Line motion")

xpy.control.initialize(experiment)


line = xpy.stimuli.Line(start, end, size, colour=white)
cue = xpy.stimuli.Rectangle(size=(size,size), colour=white, position=start)


line.preload()
cue.preload()

xpy.control.start()

cue.present()
experiment.clock.wait(cue_duration_ms)
line.present()
experiment.keyboard.wait()

xpy.control.end()