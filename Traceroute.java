import java.io.*;
public class Traceroute {
    public static void runCommand(String command){
        try {
            Process p = java.lang.Runtime.getRuntime().exec(command);
            BufferedReader r = new BufferedReader(new InputStreamReader(p.getInputStream()));
            String output = " ";
            while ((output = r.readLine())!=null) {
                System.out.println(output);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        try {
            runCommand("traceroute "+ args[0]);
        } catch (ArrayIndexOutOfBoundsException e) {
            System.err.println("Enter Valid hostname");
            System.exit(3);
        }
    }
}
