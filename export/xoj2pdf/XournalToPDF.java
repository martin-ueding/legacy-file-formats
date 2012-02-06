import java.awt.AWTException;
import java.awt.Robot;
import java.awt.event.KeyEvent;
import java.io.IOException;

public class XournalToPDF {
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		String infile = args[0];
		
		String[] command = {"xournal", infile};
		
		try {
			System.out.println("Starting Xournal ...");
			Runtime.getRuntime().exec(command);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		try {
			Robot r = new Robot();
			r.delay(2000);
			
			keypress(r, new int[] {KeyEvent.VK_CONTROL, KeyEvent.VK_E});
			keypress(r, new int[] {KeyEvent.VK_RIGHT});
			keypress(r, new int[] {KeyEvent.VK_PERIOD});
			keypress(r, new int[] {KeyEvent.VK_X});
			keypress(r, new int[] {KeyEvent.VK_O});
			keypress(r, new int[] {KeyEvent.VK_J});
			keypress(r, new int[] {KeyEvent.VK_ENTER});
			r.delay(500);
			keypress(r, new int[] {KeyEvent.VK_ENTER});
			r.delay(1000);
			keypress(r, new int[] {KeyEvent.VK_ALT, KeyEvent.VK_F4});
		} catch (AWTException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	public static void keypress(Robot r, int[] keycode) {
		for (int i = 0; i < keycode.length; i++) {
			int j = keycode[i];
			System.out.println("Pressing "+KeyEvent.getKeyText(j));
			r.keyPress(j);
			r.waitForIdle();
			r.delay(200);
		}
		for (int i = keycode.length-1; i >= 0; i--) {
			int j = keycode[i];
			System.out.println("Releasing "+KeyEvent.getKeyText(j));
			r.keyRelease(j);
			r.waitForIdle();
			r.delay(200);
		}
	}
}
