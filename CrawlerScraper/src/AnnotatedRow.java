import java.util.Locale;

public class AnnotatedRow {
    private int price=-1;
    private int propertyType=-1; // 1 - apt, 0 - house, -1 - not found
    private int forSale=-1; // 0 - subletting, 1 - for sale, -1 - not found
    private String location = ""; //city
    private String preciseLocation = ""; // neighborhood
    private int squareFootage=-1; // gross living area
    private int propertySquareFootage=-1; // only for houses (propertyType == 1)
    private int yearOfBuilding=-1;
    private int floor=-10; // only for apts (propertyType == 0)
    private int totalFloors=-1; // only for apts (propertyType == 0)
    private int inRegistry = -1; // 0 - no, 1 - yes, -1 - not found
    private String heating = "";
    private double numberOfRooms=-1;
    private int numberOfToilets=-1;
    private boolean parking = false;
    private boolean hasElevator = false;// only for apts (propertyType == 0)
    private boolean hasTerrace = false;// only for apts (propertyType == 0)?

    public AnnotatedRow(){
    }

    public AnnotatedRow(String price){
        this.price = Integer.parseInt(price.replaceAll("\\D", ""));
    }

    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }

    public void setPrice(String price){
        this.price = Integer.parseInt(price.replaceAll("\\D", ""));
    }

    public int getPropertyType() {
        return propertyType;
    }

    public void setPropertyType(int propertyType) {
        this.propertyType = propertyType;
    }

    public int getForSale() {
        return forSale;
    }

    public void setForSale(int forSale) {
        this.forSale = forSale;
    }

    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public String getPreciseLocation() {
        return preciseLocation;
    }

    public void setPreciseLocation(String preciseLocation) {
        this.preciseLocation = preciseLocation;
    }

    public int getSquareFootage() {
        return squareFootage;
    }

    public void setSquareFootage(int squareFootage) {
        this.squareFootage = squareFootage;
    }

    public int getPropertySquareFootage() {
        return propertySquareFootage;
    }

    public void setPropertySquareFootage(int propertySquareFootage) {
        this.propertySquareFootage = propertySquareFootage;
    }

    public int getYearOfBuilding() {
        return yearOfBuilding;
    }

    public void setYearOfBuilding(int yearOfBuilding) {
        this.yearOfBuilding = yearOfBuilding;
    }

    public int getFloor() {
        return floor;
    }

    public void setFloor(int floor) {
        this.floor = floor;
    }

    public int getTotalFloors() {
        return totalFloors;
    }

    public void setTotalFloors(int totalFloors) {
        this.totalFloors = totalFloors;
    }

    public int isInRegistry() {
        return inRegistry;
    }

    public void setInRegistry(int inRegistry) {
        this.inRegistry = inRegistry;
    }

    public String getHeating() {
        return heating;
    }

    public void setHeating(String heating) {
        this.heating = heating;
    }

    public double getNumberOfRooms() {
        return numberOfRooms;
    }

    public void setNumberOfRooms(double numberOfRooms) {
        this.numberOfRooms = numberOfRooms;
    }

    public int getNumberOfToilets() {
        return numberOfToilets;
    }

    public void setNumberOfToilets(int numberOfToilets) {
        this.numberOfToilets = numberOfToilets;
    }

    public boolean hasParking() {
        return parking;
    }

    public void setParking(boolean parking) {
        this.parking = parking;
    }

    public boolean HasElevator() {
        return hasElevator;
    }

    public void setHasElevator(boolean hasElevator) {
        this.hasElevator = hasElevator;
    }

    public boolean HasTerrace() {
        return hasTerrace;
    }

    public void setHasTerrace(boolean hasTerrace) {
        this.hasTerrace = hasTerrace;
    }

    public void setAttribute(String attributeName, String value) {
        try{
            //we ignore the properties on the website which we dont have in the database
            switch (attributeName.toLowerCase()) {
                case "površina":
                    squareFootage = Integer.parseInt(value.replaceAll("\\D", ""));
                    break;
                case "plac":
                    if (value.contains("m"))
                        propertySquareFootage = Integer.parseInt(value.replaceAll("\\D", ""));
                    else if (value.contains(".")) {
                        propertySquareFootage = (int) Math.round(Double.parseDouble(value.replaceAll("[^\\d|\\.]", "")) * 100.0);
                    } else
                        propertySquareFootage = Integer.parseInt(value.replaceAll("\\D", "")) * 100;
                    break;
                case "godina izgradnje":
                    yearOfBuilding = Integer.parseInt(value.replaceAll("\\D", ""));
                    break;
                case "spratnost":
                    if (value.contains(".")){//1. sprat
                        floor = Integer.parseInt(value.split("\\.")[0]);
                    } else{
                        String floor;
                        if (value.contains("/")){// 1/4, visoko prizemlje/5
                            String[] temp = value.split("\\/");
                            floor = temp[0];
                            totalFloors = Integer.parseInt(temp[1].replaceAll("\\D", ""));
                        } else {//podrum
                            floor = value;
                        }
                        if (floor.toLowerCase().contains("prizemlje"))
                            this.floor = 0;
                        else if (floor.toLowerCase().contains("suteren") || floor.toLowerCase().contains("podrum"))
                            this.floor = -1;
                        else if (floor.toLowerCase().contains("potkrovlje")) {
                            if (totalFloors>-1)
                                this.floor = totalFloors;
                        } else // 4 (4/7)
                            this.floor = Integer.parseInt(floor.replaceAll("\\D", ""));

                    }
                    break;
                case "uknjiženost":
                    inRegistry = (value.toLowerCase().equals("uknjiženo") || value.toLowerCase().equals("da")) ? 1 : 0;
                    break;
                case "grejanje":
                    heating = value;
                    break;
                case "broj soba":
                    numberOfRooms = Double.parseDouble(value.split(" ")[0]);
                    break;
                case "unutrašnje prostorije":
                    numberOfToilets = 0;
                    String t = value.toLowerCase();
                    if (t.contains("kupatilo"))
                        numberOfToilets++;
                    if (t.contains("kupatila (") || t.contains("kupatila(")) {
                        numberOfToilets += Integer.parseInt(t.split("kupatila")[1].split("\\)")[0].replaceAll("\\D", ""));
                    }
                    if (t.contains("toaleti")) {
                        numberOfToilets += Integer.parseInt(t.split("toaleti")[1].split("\\)")[0].replaceAll("\\D", ""));
                    } else if (t.contains("toalet")) {
                        numberOfToilets++;
                    }
                    break;
                case "parking":
                case "garaža":
                    parking = true;
                    break;
                case "lift":
                    hasElevator = true;
                    break;
                case "infrastruktura":
                    String i = value.toLowerCase();
                    if (i.contains("teras") || i.contains("lodj")
                            || i.contains("lođ") || i.contains("balkon"))
                        hasTerrace = true;
                    break;
            }
        }catch (Exception e){
            System.err.println("Something bad happened: "+e.toString());
        }
    }

    public void setTotalLocation(String totalLocation){
        String[] locations = totalLocation.split(", ");
        if (locations.length>=1)
            location = locations[locations.length-1];
        if (locations.length>=2)
            preciseLocation = locations[locations.length-2];
    }

    public void writeToDB(){
        //System.out.println(this.toString());
        Database.addToDatabase(this);

    }

    @Override
    public String toString() {
        return  "price=" + price +
                "\npropertyType=" + (propertyType==1?"apartment":(propertyType==0?"house":"not found")) +
                "\nforSale=" + (forSale==1?"for sale":(forSale==0?"for subletting":"not found")) +
                "\nlocation='" + location + '\'' +
                "\npreciseLocation='" + preciseLocation + '\'' +
                "\nsquareFootage=" + squareFootage + " m2"+
                "\npropertySquareFootage=" + propertySquareFootage + "m2"+
                "\nyearOfBuilding=" + (yearOfBuilding==-1?"not found":yearOfBuilding) +
                "\nfloor=" + floor +
                "\ntotalFloors=" + totalFloors +
                "\ninRegistry=" + (inRegistry==1?"yes":(inRegistry==0?"no":"not found")) +
                "\nheating='" + heating + '\'' +
                "\nnumberOfRooms=" + numberOfRooms +
                "\nnumberOfToilets=" + numberOfToilets +
                "\nparking=" + (parking?"yes":"not found") +
                "\nelevator=" + (hasElevator?"yes":"not found") +
                "\nterrace=" + (hasTerrace?"yes":"not found");
    }
}
