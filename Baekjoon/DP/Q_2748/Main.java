package Q_2748;
import java.io.*;

public class Main {

  static long[] arr; // 메모이제이션을 위한 값 저장소

  static long fibo(int n) {

    if (n == 0 || n == 1) {
      return n;
    }

    if (arr[n] != 0) { // 계산된 적이 있다면, 계산을 다시 하지 않는다.
      return arr[n];
    }

    arr[n] = fibo(n - 1) + fibo(n - 2);
    return arr[n];
  }

  static long fibo2(int n) {
    if (n == 0 || n == 1) {
      return n;
    } else {
      arr[0] = 0;
      arr[1] = 1;

      for (int i = 2; i < n + 1; i++) {
        arr[i] = arr[i - 1] + arr[i - 2];
      }
      return arr[n];
    }
  }

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int n = Integer.parseInt(br.readLine());

    arr = new long[n + 1];

    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    bw.write(String.valueOf(fibo(n)) + "\n");
    bw.write(String.valueOf(fibo2(n)) + "\n");

    bw.flush();
    br.close();
    bw.close();
  }
}
