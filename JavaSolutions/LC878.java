class Solution {
    public int lenLongestFibSubseq(int[] arr) {
        HashMap<Integer, List<List<Integer>>> seq = new HashMap<Integer, List<List<Integer>>>();
        HashSet<Integer> lengthOneSeq = new HashSet<Integer>();
        int res = 0;
        for (int n : arr){
            List<List<Integer>> temp = seq.getOrDefault(n, new ArrayList<>());
            for (int j = 0; j < temp.size(); j++){
                int length = temp.get(j).get(0);
                int last = temp.get(j).get(1);
                List<List<Integer>> temp2 = seq.getOrDefault(n + last, new ArrayList<>());
                temp2.add(Arrays.asList(length + 1, n));
                seq.put(n + last, temp2);
                if (length + 1 > res){
                    res = length + 1;
                }
            }

            for (int num : lengthOneSeq){
                if (lengthOneSeq.contains(n - num) && (n - num) > num){
                    List<List<Integer>> temp2 = seq.getOrDefault(n + n - num, new ArrayList<>());
                    temp2.add(Arrays.asList(3,n));
                    seq.put(n + n - num, temp2);
                    if (res < 3){
                        res = 3;
                    }
                }
            }
            lengthOneSeq.add(n);
            // System.out.println(seq);
        }
        return res;
    }
}