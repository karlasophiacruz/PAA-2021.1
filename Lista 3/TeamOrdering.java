import java.util.*;

class Result {
    int winner;
    int loser;
  
    Result(int winner, int loser)
    {
        this.winner = winner;
        this.loser = loser;
    }
}

public class TeamOrdering {

    static void arrangeTeams(int[] teams, Result[] results) {
        HashMap<Integer, List<Integer>> map = new HashMap<>();
        int winner = 0;
  
        for (int i = 0; i < results.length; i++) {
            winner = results[i].winner;
            if (map.containsKey(winner)) {
                map.get(winner).add(
                    results[i].loser);
            }
            else {
                List<Integer> list
                    = new ArrayList<Integer>();
                list.add(results[i].loser);
                map.put(winner, list);
            }
        }
        List<Integer> output = new ArrayList<>();
 
        setInOrder(teams, map, teams.length, output);
        Iterator<Integer> it = output.iterator();
  
        while (it.hasNext()) {
            System.out.print(it.next());
            System.out.print(" ");
        }
    }
  
    static void setInOrder(int[] teams, HashMap<Integer, List<Integer> > map, int n, List<Integer> output) {
        if (n < 1) {
            return;
        }
        else if (n == 1) {
            output.add(teams[n - 1]);
            return;
        }
  
        setInOrder(teams, map, n - 1, output);
        int key = teams[n - 1];
        int i;
  
        for (i = 0; i < output.size(); i++) {
  
            int team = output.get(i);
  
            List<Integer> losers = map.get(key);
            if (losers.indexOf(team) != -1)
                break;
        }
        output.add(i, key);
    }
  
    public static void main(String[] args) {
        int[] teams = { 1, 2, 3, 4 };
        Result[] results = {
            new Result(1, 4),
            new Result(4, 3),
            new Result(2, 3),
            new Result(1, 2),
            new Result(2, 1),
            new Result(3, 1),
            new Result(2, 4)
        };
  
        arrangeTeams(teams, results);
    }
}