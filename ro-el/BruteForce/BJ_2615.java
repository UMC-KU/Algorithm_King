package BruteForce;

// 오목

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BJ_2615 {
    // Index 벗어나는 것을 방지하기 위하여 21로 0 ~ 20 - 실제 데이터는 1 ~ 19
    static int[][] map = new int[21][21];
    static int[][][] memoCnt = new int[21][21][4];
    static int[] dx = new int[] {1, 1, 0, -1};
    static int[] dy = new int[] {0, 1, 1, 1};

    public static int calculate(int i, int j, int d, int color){
        int nx = i + dx[d];
        int ny = j + dy[d];

        if(map[nx][ny] != color)
            return 1;
        else
            return memoCnt[nx][ny][d] = calculate(nx, ny, d, color) + 1;
        // 같은 색의 돌이 존재하는 한 방향에 대한 재귀 탐색
        // 다른 색의 돌을 마주쳤을 때부터 1을 더해
        // 동일한 색이 몇 개 이어졌는지 return
    }

    public static String WhoWinOrNot(){
        for(int j=1; j<20; j++){
            for(int i=1; i<20; i++){
                // 여기서 i, j 위치 바뀌면 왜 안되는지?
                if(map[i][j] == 1 || map[i][j] == 2){
                    for(int k=0; k<4; k++){
                        if(memoCnt[i][j][k] == 0 && calculate(i, j, k, map[i][j]) == 5)
                            // 같은 색의 돌이 몇 개 이어졌는지 판단, 그 수가 5보다 크면
                            // (6개 이상 연속적으로 놓인 경우는 이긴 것이 아니기 때문)
                            // 돌의 색과 시작 위치 반환
                            return map[i][j] + "\n" + i + " " + j;
                    }
                }
            }
        }
        return "0";
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        // 0: 없음, 1: 흑돌, 2: 백돌
        for(int i=1; i<20; i++){
            st = new StringTokenizer(br.readLine());
            for(int j=1; j<20; j++)
                map[i][j] = Integer.parseInt(st.nextToken());
        }

        System.out.print(WhoWinOrNot());
    }
}
