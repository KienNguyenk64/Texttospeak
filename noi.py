import pyttsx3

robot_brain = "A newspaper is a periodical publication containing written information about current events and is often typed in black ink with a white or gray background. Newspapers can cover a wide variety of fields such as politics, business, sports, art, and science. They often include materials such as opinion columns, weather forecasts, reviews of local services, obituaries, birth notices, crosswords, editorial cartoons, comic strips, and advice columns."
robot_mounth = pyttsx3.init()
robot_mounth.say(robot_brain)
robot_mounth.runAndWait()