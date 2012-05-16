// Copyright (c) 2012 Martin Ueding <dev@martin-ueding.de>

import java.awt.AWTException;
import java.awt.Robot;
import java.awt.event.KeyEvent;
import java.io.IOException;

/**
 * Converts the given Xournal notebook into a PDF.
 *
 * See README.markdown in this folder for more information.
 *
 * @author Martin Ueding <dev@martin-ueding.de>
 */
public class XournalToPDF {
	/**
	 * @param args Command line arguments.
	 */
	public static void main(String[] args) {
		String xournalFile = args[0];

		String[] xournalStartCommand = {"xournal", xournalFile};

		try {
			System.out.println("Starting Xournal ...");
			Runtime.getRuntime().exec(xournalStartCommand);
		}
		catch (IOException e) {
			e.printStackTrace();
		}

		try {
			Robot robot = new Robot();

			// Wait until Xournal is loaded.
			robot.delay(10000);

			// Open the Export dialog.
			keypress(robot, new int[] {KeyEvent.VK_CONTROL, KeyEvent.VK_E});

			// Type in ".xoj".
			keypress(robot, new int[] {KeyEvent.VK_RIGHT});
			keypress(robot, new int[] {KeyEvent.VK_PERIOD});
			keypress(robot, new int[] {KeyEvent.VK_X});
			keypress(robot, new int[] {KeyEvent.VK_O});
			keypress(robot, new int[] {KeyEvent.VK_J});

			// Save.
			keypress(robot, new int[] {KeyEvent.VK_ENTER});
			robot.delay(500);

			// Yes, overwrite.
			keypress(robot, new int[] {KeyEvent.VK_ENTER});
			robot.delay(1000);

			// Close Xournal.
			keypress(robot, new int[] {KeyEvent.VK_ALT, KeyEvent.VK_F4});
			robot.delay(500);
		}
		catch (AWTException e) {
			e.printStackTrace();
		}
	}

	/**
	 * Lets the robot press the keys in order and release them in reverse.
	 *
	 * @param robot Robot to use.
	 * @param keyCodes Array with KeyCode to press.
	 */
	public static void keypress(Robot robot, int[] keyCodes) {
		// Press the keys.
		for (int i = 0; i < keyCodes.length; i++) {
			int keyCode = keyCodes[i];
			System.out.println("Pressing " + KeyEvent.getKeyText(keyCode));
			robot.keyPress(keyCode);
			robot.waitForIdle();
			robot.delay(200);
		}

		// Release them in reverse order.
		for (int i = keyCodes.length - 1; i >= 0; i--) {
			int keyCode = keyCodes[i];
			System.out.println("Releasing " + KeyEvent.getKeyText(keyCode));
			robot.keyRelease(keyCode);
			robot.waitForIdle();
			robot.delay(200);
		}
	}
}
