public class card {
    private final String face;
    private final String suit;

        public card(String face, String suit)
        {
            this.face = face;
            this.suit = suit;
        }
        
        public String toString()
        {
            return face + " of " + suit;
        }    
}
