🧙‍♂️ The Magical Blue Invisibility Cloak 🧙‍♀️
Show Image
Show Image
Show Image
<p align="center">
  <img src="https://media.tenor.com/4tC_NBki6UUAAAAM/harry-potter-daniel-radcliffe.gif" alt="Magic Animation" width="300"/>
</p>
✨ The Magic Revealed
Ever wanted to be invisible like Harry Potter? Now you can be! This project uses computer vision to create a "magic invisibility cloak" effect using any blue fabric.
The magic spell works like this:

The camera captures what's behind you
When you appear with something blue, those blue pixels are replaced with the background
Voila! You appear to be invisible wherever the blue cloth covers you!

<p align="center">
  <img src="https://media.tenor.com/N4BdiKlPp3cAAAAM/im-invisible-invisible.gif" alt="Invisibility Demo" width="400"/>
</p>
🪄 Magic Ingredients (Requirements)

Python 3.6 or higher
OpenCV library
NumPy
A webcam
A piece of blue fabric (the more vibrant the blue, the better the magic works!)

🧪 Potion Instructions (Installation)

Clone this magical repository:

bashCopygit clone https://github.com/yourusername/blue-invisibility-cloak.git
cd blue-invisibility-cloak

Install the magical dependencies:

bashCopypip install opencv-python numpy

That's it! No eye of newt or toe of frog needed.

🔮 Casting the Spell (Usage)

Run the magic spell:

bashCopypython blue_invisibility.py

Step away from the camera's view (the spell needs to capture the background)
Wait for the 3-second countdown
Step back into view with your blue cloth and watch the magic happen!
Press 'q' to break the spell and exit


🧙 Advanced Spellcasting (Customization)
Want to adjust the magic for different shades of blue or lighting conditions?
Modify these lines in the code:
pythonCopy# Define range for blue color in HSV
lower_blue = np.array([90, 50, 50])
upper_blue = np.array([130, 255, 255])

For lighter blue: decrease the lower bound's first value
For darker blue: increase the upper bound's first value
For better detection in low light: decrease the second and third values in the lower bound

🧬 How the Magic Works
The spell uses the ancient art of HSV color space transformation and mask creation:

Background Capture: The spell first memorizes what's behind you
Color Detection: It identifies blue objects using HSV color space
Masking: Creates a magical stencil showing where blue appears
Background Substitution: Replaces blue areas with the background
Result: You appear to vanish wherever the blue cloth covers you!

<p align="center">
  <img src="https://media.giphy.com/media/l0MYEqEzwMWFCg8rm/giphy.gif" alt="Science Magic" width="350"/>
</p>
🌈 Try Other Magic Colors!

Want to try a different color of invisibility? Modify the HSV values:

Red: lower_red = np.array([0, 50, 50]) and upper_red = np.array([10, 255, 255])
Green: lower_green = np.array([40, 50, 50]) and upper_green = np.array([80, 255, 255])
Purple: lower_purple = np.array([130, 50, 50]) and upper_purple = np.array([170, 255, 255])


🧙‍♂️ Credits and Acknowledgments

Inspired by the invisibility cloak from Harry Potter
Created using the powerful wizardry of OpenCV
Developed by Antonela - a modern-day tech wizard

⭐ If this magic brought a smile to your face, please star this repository! ⭐
<p align="center">Made with ❤️ and a bit of magic ✨</p>