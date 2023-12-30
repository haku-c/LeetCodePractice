import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;

public class LC802 {
    // detect cycle
    public boolean dfs(List<List<Integer>> graph, int node, boolean[] visitedInPath, boolean[] visited, boolean[] cycle) {
        visitedInPath[node] = visited[node] = true;
        for (int adj : graph.get(node)) {
            if (!visited[adj]) {
                if (dfs(graph, adj, visitedInPath, visited, cycle)) return cycle[node] = true;
            } else if (visitedInPath[adj]) {
                return cycle[node] = true;
            }
        }
        visitedInPath[node] = false;
        return false;
    }

    public List<Integer> eventualSafeNodes(int[][] graph) {
        int len = graph.length;
        List<List<Integer>> adjList = new ArrayList<>();
        for (int i = 0; i < len; i++) {
            adjList.add(new ArrayList<>());
        }
        for (int i = 0; i < len; i++) {
            for (int j = 0; j < graph[i].length; j++) {
                adjList.get(i).add(graph[i][j]);
            }
        }

        List<Integer> res = new ArrayList<>();
        // default value should be false for both
        boolean[] visited = new boolean[len];
        boolean[] cycle = new boolean[len];
        boolean[] path = new boolean[len];

        for (int i = 0; i < len; i++) {
            if (!visited[i]) {
                dfs(adjList, i, path, visited, cycle);
            }
        }
        for (int i = 0; i < len; i++) {
            if (!cycle[i]) {
                res.add(i);
            }
        }
        return res;
    }
}
