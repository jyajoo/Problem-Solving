package Q_2072;

import java.util.Scanner;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T;
		T = sc.nextInt();

		// 10개의 수를 입력 받아, 그 중에서 홀수만 더한 값을 출력하는 프로그램을 작성하라.
		for(int test_case = 1; test_case <= T; test_case++)
		{
			int answer = 0;
			for (int i = 0; i < 10; i++) {
				int number = sc.nextInt();
				if (number % 2 != 0) {
					answer += number;
				}
			}
			System.out.println("#" + test_case + " " + answer);
		}
	}
}