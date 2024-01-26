int[][][] numPaths;

    public int findPaths(int m, int n, int maxMove, int startRow, int startColumn) {
        numPaths= new int[m][n][maxMove+1];

        for(int[][] arr2d:numPaths){
            for(int[] arr:arr2d){
                Arrays.fill(arr,-1);
            }
        }
        
        return recurse(m, n, startRow, startColumn, maxMove);

    }

    public int recurse(int m, int n, int startRow, int startColumn, int numMoves) {
        if (startRow < 0||startColumn == n || startColumn < 0||startRow == m ) return 1;
        if(numMoves==0) return 0;
        if(numPaths[startRow][startColumn][numMoves]>=0) return numPaths[startRow][startColumn][numMoves];

        numPaths[startRow][startColumn][numMoves] = ((recurse(m, n, startRow - 1, startColumn, numMoves - 1)+recurse(m, n, startRow + 1, startColumn, numMoves - 1))% 1000000007+(recurse(m, n, startRow, startColumn + 1, numMoves - 1)+recurse(m, n, startRow, startColumn - 1, numMoves - 1))% 1000000007)% 1000000007;
        return numPaths[startRow][startColumn][numMoves];
    }
