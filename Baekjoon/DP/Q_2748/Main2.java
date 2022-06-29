package Q_2748;

import java.io.*;

public class Main2 {
  static long fibo(int n) {

    long[] arr = { 0, 1 };
    long answer = 0;

    if (n == 0 || n == 1) {
      return n;
    }
    for (int i = 2; i < n + 1; i++) {
      answer = arr[0] + arr[1];
      arr[0] = arr[1];
      arr[1] = answer;
    }
    return answer;
  }

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int n = Integer.parseInt(br.readLine());

    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    bw.write(String.valueOf(fibo(n)) + "\n");

    bw.flush();
    br.close();
    bw.close();
  }
}
