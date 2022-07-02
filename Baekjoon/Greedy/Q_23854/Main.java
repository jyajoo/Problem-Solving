import java.io.*;

public class Main {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    int a = Integer.parseInt(br.readLine());
    int b = Integer.parseInt(br.readLine());

    int a_win = 0;
    int draw = 0;
    int b_win = 0;

    if (a >= 3) {
      a_win = a / 3;
      a = a % 3;
    }

    if (b >= 3) {
      b_win = b / 3;
      b = b % 3;
    }

    if (a == b) {
      draw = a;
      bw.write(a_win + " " + draw + " " + b_win);
    } else {
      bw.write(String.valueOf(-1)); // bw에서 정수형 출력 시, String을로 감싸기
    }

    bw.flush();
    br.close();
    bw.close();
  }
}