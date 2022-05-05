package BruteForce;

// 숫자 야구

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.ArrayList;

public class BJ_2503 {
    static int isFirst=0;
    static ArrayList<Integer> finalArr = new ArrayList<>();
    // 최종 가능한 숫자 집어넣음
    // -> 각 숫자마다 가능한 숫자 temp ArrayList에 넣고 비교

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[] data = new int[3]; // data[0] : 100의 자리, data[1] : 10의 자리, data[2] : 1의 자리

        for(int i=0; i<N; i++){
            String str;
            int strike, ball;

            StringTokenizer st = new StringTokenizer(br.readLine());
            str = st.nextToken();
            for(int j=0; j<3; j++)
                data[j] = Character.getNumericValue(str.charAt(j));
            strike = Integer.parseInt(st.nextToken());
            ball = Integer.parseInt(st.nextToken());

            // 가능한 숫자 추출
            whatNumber(data, strike, ball);
        }

        System.out.print(finalArr.size());
    }

    public static void whatNumber(int[] data, int strike, int ball){
        ArrayList<Integer> tempArr = new ArrayList<>();

        isFirst++;

        for(int i=123; i<=987; i++){
            int testStrike=0, testBall=0;
            int[] tempData = new int[3];

            tempData[0] = i/100;
            tempData[1] = (i%100)/10;
            tempData[2] = i%10;

            // 0이 포함된 숫자 제외
            if(tempData[1]==0 || tempData[2]==0)
                continue;

            // 같은 수가 여러 자리에 속한 숫자 제외
            if(tempData[0] == tempData[1] || tempData[1] == tempData[2] || tempData[0] == tempData[2])
                continue;

            for(int j=0; j<3; j++){
                for(int k=0; k<3; k++){
                    if(data[j] == tempData[k]){ // 같은 숫자가 존재할 때
                        if(j==k) // 위치까지 같으면 testStrike count +1
                            testStrike++;
                        else // 다르면 testBall count +1
                            testBall++;
                    }
                }
            }

            if(testStrike == strike && testBall == ball)
                tempArr.add(i);
        }

        if(isFirst==1)
            finalArr.addAll(tempArr);
        else
            finalArr.retainAll(tempArr);
    }
}
