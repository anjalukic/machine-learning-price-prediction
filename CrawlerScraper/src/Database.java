import java.sql.*;

public class Database {
    private static Connection conn;
    public static String db_url = "jdbc:mysql://localhost:3306/nekretnine";
    public static String user = "root";
    public static String psw = "root";

    public static void initialize(){
        // Open a connection and create a table
        try(Connection conn = DriverManager.getConnection(db_url, user, psw);
            Statement stmt = conn.createStatement();
        ) {
            Database.conn = conn;
            System.out.println("Connection to the database established");
            String sql = "DROP TABLE realestate";
            stmt.executeUpdate(sql);
            sql = "CREATE TABLE `nekretnine`.`realestate` (" +
                    "  `id` INT NOT NULL AUTO_INCREMENT," +
                    "  `propertyType` TINYINT NULL," +
                    "  `forSale` TINYINT NULL," +
                    "  `price` INT NULL," +
                    "  `location` VARCHAR(45) NULL," +
                    "  `preciseLocation` VARCHAR(45) NULL," +
                    "  `squareFootage` INT NULL," +
                    "  `propertySquareFootage` INT NULL," +
                    "  `yearOfBuilding` INT NULL," +
                    "  `floor` INT NULL," +
                    "  `totalFloors` INT NULL," +
                    "  `inRegistry` TINYINT NULL," +
                    "  `heating` VARCHAR(45) NULL," +
                    "  `numberOfRooms` DOUBLE NULL," +
                    "  `numberOfToilets` INT NULL," +
                    "  `parking` TINYINT NULL," +
                    "  `hasElevator` TINYINT NULL," +
                    "  `hasTerrace` TINYINT NULL," +
                    "  PRIMARY KEY (`id`)," +
                    "  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE);";
            stmt.executeUpdate(sql);
            System.out.println("Table created");
        } catch (SQLException e) {
            System.out.println("Error ocurred");
        }

    }

    public static void addToDatabase(AnnotatedRow row){

        // if parking, elevator or terrace is false -> leave the column in db empty
        String sql = "insert into realestate (propertyType, forSale, price, location, preciseLocation,squareFootage, " +
                "propertySquareFootage, yearOfBuilding, floor, totalFloors, inRegistry, heating, numberOfRooms, numberOfToilets, " +
                "parking, hasElevator, hasTerrace) " +
                "values (?,?,?, ?, ?, ?, ?, ?,?,?,?,?, ?, ?, ?,?,?)";
        /*try(PreparedStatement stmt = conn.prepareStatement(sql);
        ) {

           // stmt.executeUpdate();
        } catch (SQLException e) {
            System.out.println("Error ocurred");
        }*/
    }
}
