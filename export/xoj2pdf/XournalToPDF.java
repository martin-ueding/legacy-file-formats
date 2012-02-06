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
		
		

	}
}
