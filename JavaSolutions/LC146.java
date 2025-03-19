class Node {
    public int value;
    public int key;
    public Node next;
    public Node last;

    public Node(int key, int val){
        this.value = val;
        this.key = key;
        this.next = null;
        this.last = null;
    }
}

class LRUCache {
    private Node head;
    private Node tail;
    private Integer capacity;
    private HashMap<Integer, Node> cache;

    public LRUCache(int capacity) {
        this.head = new Node(-1,-1);
        this.tail = new Node(-1,-1);
        this.head.next = this.tail;
        this.tail.last = this.head;
        this.capacity = capacity;
        this.cache = new HashMap<>();
    }

    private void delete(Node node){
        node.last.next = node.next;
        node.next.last = node.last;
    }

    private void insert(Node node){
        Node second = this.head.next;
        this.head.next = node;
        second.last = node;
        node.next = second;
        node.last = this.head;
    }

    public int get(int key) {
        if (this.cache.containsKey(key)){
            Node current = this.cache.get(key);
            this.delete(current);
            this.insert(current);
            return current.value;
        }
        return -1;
    }
    
    public void put(int key, int value) {
        Node current;
        if (this.cache.containsKey(key)){
            current = this.cache.get(key);
            current.value = value;
            this.delete(current);
        } else if (this.cache.size() == this.capacity){
            Node lastNode = this.tail.last;
            this.delete(lastNode);
            this.cache.remove(lastNode.key);
            current = new Node(key, value);
        } else {
            current = new Node(key, value);
        }
        // move current node to front
        this.insert(current);
        this.cache.put(key, current);
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */