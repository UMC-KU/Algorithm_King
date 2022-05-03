package DataStructure;

// 괄호

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BJ_9012 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int n;

        int N = Integer.parseInt(br.readLine());

        for(int i=0; i<N; i++){
            n=0;
            String str = br.readLine();
            for(int j=0; j<str.length(); j++){
                char ch = str.charAt(j);
                if(ch=='(')
                    n++;
                else{
                    n--;
                    if(n<0)
                        break;
                }
            }
            if(n==0)
                sb.append("YES\n");
            else
                sb.append("NO\n");
        }
        System.out.print(sb);
    }
}