package DataStructure;

// 요세푸스 문제

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BJ_1158 {
    public static void main(String[] args) throws IOException{
        StringBuilder sb = new StringBuilder();
        sb.append("<");
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        Queue<Integer> que = new LinkedList<>();

        int N, K;

        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        for(int i=1; i<=N; i++)
            que.offer(i);

        while(!que.isEmpty()){
            for(int j=0; j<K-1; j++)
                que.offer(que.poll());
            sb.append(que.poll() + ", ");
        }

        sb.delete(sb.length()-2, sb.length());
        sb.append(">");
        System.out.println(sb);
    }
}
