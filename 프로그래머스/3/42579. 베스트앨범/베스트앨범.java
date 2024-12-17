import java.util.*;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        List<Song> songList = new ArrayList<>();
        Map<String, Integer> map = new HashMap<>();

        for (int i = 0; i < genres.length; i++) {
            map.put(genres[i], map.getOrDefault(genres[i], 0) + plays[i]);
            songList.add(new Song(genres[i], plays[i], i));
        }

        ArrayList<String> mapSortKey = new ArrayList<>(map.keySet());
        mapSortKey.sort(new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                return map.get(o2).compareTo(map.get(o1));
            }
        });
        songList.sort(null);


        List<Integer> temp = new ArrayList<>();
        for (String key : mapSortKey) {
            int count = 0;
            for (Song song : songList) {
                if (key.equals(song.genre)) {
                    temp.add(song.number);
                    count++;
                }
                if (count == 2) {
                    break;
                }
            }
        }

        int[] answer = temp.stream()
                .mapToInt(t -> t.intValue()).toArray();
        return answer;
    }
}

class Song implements Comparable<Song> {
    String genre;
    int play;
    int number;

    public Song(String genre, int play, int number) {
        this.genre = genre;
        this.play = play;
        this.number = number;
    }

    @Override
    public int compareTo(Song s) {
        if (this.play != s.play) {
            return Integer.compare(this.play, s.play) * -1;
        }
        return Integer.compare(this.number, s.number);
    }
}