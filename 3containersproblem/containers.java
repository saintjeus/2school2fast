import java.util.Stack;

public class containers {
    public int sizeA;
    public int sizeB;
    public int sizeC;
    int container[][][];

    public containers(){
        sizeA = 10;
        sizeB = 7;
        sizeC = 4;
        container = new int [sizeA+1][sizeB+1][sizeC+1];
    }


    private void reset(){
        for (int i = 0; i < (sizeA+1); i++)
            for (int j = 0; j < (sizeB+1); j++)
                for (int k = 0; k < (sizeC+1); k++) {
                    container[i][j][k] = 0;
                }
    }

    void startpour(int a, int b, int c, int endA, int endB, int endC){
        Stack<String> path = new Stack<String>();
        path.push("("+a+", "+b+", "+c+")");
        pouring(a, b, c, endA, endB, endC, path);
        if (container[endA][endB][endC]==0)
            System.out.println("No sequence of pourings from ("+a+","+b+","+c+") to ("+endA+","+endB+","+endC+").\n");
    }
    void pouring (int a, int b, int c, int endA, int endB, int endC, Stack<String> path){
        int tempA, tempB, tempC;

        container[a][b][c] = 1; //vertex is visited = true
        if (a == endA && b == endB && c==endC) {
            //if we've reached the vertex, print the path
            String graphpath = "";
            while (!path.empty()) {
                graphpath = path.pop() + ", "+graphpath;
            }
            graphpath = graphpath.substring(0, graphpath.length()-2);
            System.out.println(graphpath);
            System.out.println();
            return;
        }

        //AtoB
        if ((a>0)&&(b<sizeB)) {
            tempA = a;
            tempB = b;
            while ((tempA > 0) && (tempB < sizeB)) {
                tempA--;
                tempB++;
            }
            if (container[tempA][tempB][c] == 0) {
                path.push("(" + tempA + ", " + tempB + ", " + c + ")");
                pouring(tempA, tempB, c, endA, endB, endC, path);
                if (!path.empty()) {
                    path.pop();
                }
                else
                    return;
            }
        }

        //AtoC
        if ((a>0)&&(c<sizeC)) {
            tempA = a;
            tempC = c;
            while ((tempA > 0) && (tempC < sizeC)) {
                tempA--;
                tempC++;
            }//end while
            if (container[tempA][b][tempC] == 0) {
                path.push("(" + tempA + ", " + b + ", " + tempC + ")");
                pouring(tempA, b, tempC, endA, endB, endC, path);
                if (!path.empty()) {
                    path.pop();
                }
                else
                    return;
            }
        }

        //BtoA
        if ((b>0)&&(a<sizeA)) {
            tempA = a;
            tempB = b;
            while ((tempB > 0) && (tempA < sizeA)) {
                tempB--;
                tempA++;
            }//end while
            if (container[tempA][tempB][c] == 0) {
                path.push("(" + tempA + ", " + tempB + ", " + c + ")");
                pouring(tempA, tempB, c, endA, endB, endC, path);
                if (!path.empty()){
                path.pop();}
                else
                    return;
            }
        }
        //BtoC
        if ((b>0)&&(c<sizeC)) {
            tempB = b;
            tempC = c;
            while ((tempB > 0) && (tempC < sizeC)) {
                tempB--;
                tempC++;
            }//end while
            if (container[a][tempB][tempC] == 0) {
                path.push("(" + a + ", " + tempB + ", " + tempC + ")");
                pouring(a, tempB, tempC, endA, endB, endC, path);
                if (!path.empty()) {
                    path.pop();
                }
                else
                    return;
            }
        }
        //CtoA
        if ((c>0)&&(a<sizeA)) {
            tempC = c;
            tempA = a;
            while ((tempC > 0) && (tempA < sizeA)) {
                tempC--;
                tempA++;
            }//end while
            if (container[tempA][b][tempC] == 0) {
                path.push("(" + tempA + ", " + b + ", " + tempC + ")");
                pouring(tempA, b, tempC, endA, endB, endC, path);
                if (!path.empty()) {
                    path.pop();
                }
                else
                    return;
            }
        }
        //CtoB
        if ((c>0)&&(b<sizeB)) {
            tempC = c;
            tempB = b;
            while ((tempC > 0) && (tempB < sizeB)) {
                tempC--;
                tempB++;
            }//end while
            if (container[a][tempB][tempC] == 0) {
                path.push("(" + a + ", " + tempB + ", " + tempC + ")");
                pouring(a, tempB, tempC, endA, endB, endC, path);
                if (!path.empty())
                path.pop();
                else
                    return;
            }//end if
        }//end if
    }//end pouring

    public static void main (String[] args){
        containers containers = new containers();

        System.out.println("Input (0,7,4,2,7,2)");
        containers.startpour(0,7,4,2,7,2);
        containers.reset();

        System.out.println("Input (10,0,4,2,7,2)");
        containers.startpour(10,0,4,2,7,2);
        containers.reset();

        System.out.println("Input (8,6,3,7,6,4)");
        containers.startpour(8,6,3,7,6,4);
        containers.reset();

        System.out.println("Input (1,7,4,3,6,2)");
        containers.startpour(1,7,4,3,6,2);
        containers.reset();

        System.out.println("Input (2,7,4,3,6,2)");
        containers.startpour(2,7,4,3,6,2);
        containers.reset();

        System.out.println("Input (6,3,3,3,6,3)");
        containers.startpour(6,3,3,3,6,3);

    }
}