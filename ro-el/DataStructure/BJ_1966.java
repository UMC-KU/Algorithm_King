package DataStructure;

// 프린터 큐

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BJ_1966 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int T, N, M;

        T = Integer.parseInt(br.readLine());

        for(int i=0; i<T; i++){
            int cnt=0;

            StringTokenizer st = new StringTokenizer(br.readLine());
            N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());

            // 테스트 케이스 별 Queue - 처음 위치, 우선 순위
            Queue<int[]> que = new LinkedList<>();
            int[] priority = new int[N];

            st = new StringTokenizer(br.readLine());
            for(int j=0; j<N; j++){
                int temp = Integer.parseInt(st.nextToken());
                que.offer(new int[]{j, temp});
                priority[j] = temp;
            }

            Arrays.sort(priority);

            int where = N-1;

            while(!que.isEmpty()){
                int[] temp = que.poll();

                if(temp[1] == priority[where]){
                    cnt++;
                    if(temp[0] == M){
                        sb.append(cnt+"\n");
                        break;
                    }
                    where--;
                }
                else
                    que.offer(temp);
            }
        }

        System.out.print(sb);
    }
}
