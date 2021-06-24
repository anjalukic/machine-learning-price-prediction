import java.util.Locale;

public class AnnotatedRow {
    private int price;
    private boolean propertyType; // true - apt, false - house
    private boolean forSale; // 0 - subletting, 1 - for sale
    private String location = ""; //city
    private String preciseLocation = ""; // neighborhood
    private int squareFootage; // gross living area
    private int propertySquareFootage; // only for houses (propertyType == 1)
    private int yearOfBuilding;
    private int floor; // only for apts (propertyType == 0)
    private int totalFloors; // only for apts (propertyType == 0)
    private boolean inRegistry = false;
    private String heating = "";
    private double numberOfRooms;
    private int numberOfToilets;
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

    public boolean getPropertyType() {
        return propertyType;
    }

    public void setPropertyType(boolean propertyType) {
        this.propertyType = propertyType;
    }

    public boolean getForSale() {
        return forSale;
    }

    public void setForSale(boolean forSale) {
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

    public boolean isInRegistry() {
        return inRegistry;
    }

    public void setInRegistry(boolean inRegistry) {
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

    public void setAttribute(String attributeName, String value){
        //we ignore the properties on the website which we dont have in the database
        switch (attributeName.toLowerCase()) {
            case "površina":
                squareFootage = Integer.parseInt(value.replaceAll("\\D", ""));
                break;
            case "plac":
                if (value.contains("m"))
                    propertySquareFootage = Integer.parseInt(value.replaceAll("\\D", ""));
                else
                    propertySquareFootage = Integer.parseInt(value.replaceAll("\\D", ""))*100;
                break;
            case "godina izgradnje":
                yearOfBuilding = Integer.parseInt(value.replaceAll("\\D", ""));
                break;
            case "spratnost":
                String[] floors = (value.split(" ")[0]).split("\\/");
                if (floors[0].toLowerCase().contains("prizemlje"))
                    floor = 0;
                else if (floors[0].toLowerCase().contains("suteren"))
                    floor = -1;
                else
                    floor = Integer.parseInt(floors[0].replaceAll("\\.",""));
                if (floors.length>1)
                    totalFloors = Integer.parseInt(floors[1]);
                break;
            case "uknjiženost":
                inRegistry = (value.toLowerCase().equals("uknjiženo") || value.toLowerCase().equals("da"))?true:false;
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
                if (t.contains("kupatila (") || t.contains("kupatila(")){
                    numberOfToilets+=Integer.parseInt(t.split("kupatila")[1].split("\\)")[0].replaceAll("\\D", ""));
                }
                if (t.contains("toaleti")){
                    numberOfToilets+=Integer.parseInt(t.split("toaleti")[1].split("\\)")[0].replaceAll("\\D", ""));
                }
                if (t.contains("kupatilo")){
                    numberOfToilets++;
                }
                break;
            case "parking": case "garaža":
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
    }

    public void setTotalLocation(String totalLocation){
        String[] locations = totalLocation.split(", ");
        if (locations.length>=1)
            location = locations[locations.length-1];
        if (locations.length>=2)
            preciseLocation = locations[locations.length-2];
    }

    public void writeToDB(){
        System.out.println(this.toString());
        Database.addToDatabase(this);

    }

    @Override
    public String toString() {
        return  "price=" + price +
                "\npropertyType=" + (propertyType?"apartment":"house") +
                "\nforSale=" + (forSale?"for sale":"for subletting") +
                "\nlocation='" + location + '\'' +
                "\npreciseLocation='" + preciseLocation + '\'' +
                "\nsquareFootage=" + squareFootage + " m2"+
                "\npropertySquareFootage=" + propertySquareFootage + "m2"+
                "\nyearOfBuilding=" + yearOfBuilding +
                "\nfloor=" + floor +
                "\ntotalFloors=" + totalFloors +
                "\ninRegistry=" + (inRegistry?"yes":"no") +
                "\nheating='" + heating + '\'' +
                "\nnumberOfRooms=" + numberOfRooms +
                "\nnumberOfToilets=" + numberOfToilets +
                "\nparking=" + (parking?"yes":"no") +
                "\nelevator=" + (hasElevator?"yes":"no") +
                "\nterrace=" + (hasTerrace?"yes":"no");
    }
}
