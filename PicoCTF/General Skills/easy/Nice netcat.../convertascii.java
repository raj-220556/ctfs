// print Ascii Contented file as normal text


import java.io.*;

class concvertascii{
  public static void main(String args[]) throws IOException{
    FileReader fr = new FileReader("solution.txt");
    BufferedReader br = new BufferedReader(fr);

    String line = br.readLine();
    while(line != null){
      Integer p = Integer.valueOf(line);
      System.out.print((char)(int)p);
      line = br.readLine();
    }
  }
}

