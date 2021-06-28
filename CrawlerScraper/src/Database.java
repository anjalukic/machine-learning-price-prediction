import java.sql.*;

public class Database {
    private static int counter = 0;
    private static Connection conn;
    public static String db_url = "jdbc:mysql://localhost:3306/nekretnine";
    public static String user = "root";
    public static String psw = "root";

    public static void initialize(){
        // Open a connection and create a table
        try{
            Connection conn = DriverManager.getConnection(db_url, user, psw);
            Statement stmt = conn.createStatement();
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

        String sql = "insert into realestate (propertyType, forSale, price, location, preciseLocation,squareFootage,propertySquareFootage, " +
                "yearOfBuilding, floor, totalFloors, inRegistry, heating, numberOfRooms, numberOfToilets,parking, hasElevator, hasTerrace) " +
                "values (?,?,?, ?, ?, ?, ?, ?,?,?,?,?, ?, ?, ?,?,?)";

        try(PreparedStatement stmt = conn.prepareStatement(sql);
        ) {
            if (row.getPropertyType() != -1) stmt.setInt(1, row.getPropertyType());
            else stmt.setNull(1, Types.TINYINT);
            if (row.getForSale() != -1) stmt.setInt(2, row.getForSale());
            else stmt.setNull(2, Types.TINYINT);
            if (row.getPrice() != -1) stmt.setInt(3, row.getPrice());
            else stmt.setNull(3, Types.INTEGER);
            if (!row.getLocation().equals("")) stmt.setString(4, row.getLocation());
            else stmt.setNull(4, Types.VARCHAR);
            if (!row.getPreciseLocation().equals("")) stmt.setString(5, row.getPreciseLocation());
            else stmt.setNull(5, Types.VARCHAR);
            if (row.getSquareFootage() != -1) stmt.setInt(6, row.getSquareFootage());
            else stmt.setNull(6, Types.INTEGER);
            if (row.getPropertySquareFootage() != -1) stmt.setInt(7, row.getPropertySquareFootage());
            else stmt.setNull(7, Types.INTEGER);
            if (row.getYearOfBuilding() != -1) stmt.setInt(8, row.getYearOfBuilding());
            else stmt.setNull(8, Types.INTEGER);
            if (row.getFloor() != -10) stmt.setInt(9, row.getFloor());
            else stmt.setNull(9, Types.INTEGER);
            if (row.getTotalFloors() != -1) stmt.setInt(10, row.getTotalFloors());
            else stmt.setNull(10, Types.INTEGER);
            if (row.isInRegistry() != -1) stmt.setInt(11, row.isInRegistry());
            else stmt.setNull(11, Types.TINYINT);
            if (!row.getHeating().equals("")) stmt.setString(12, row.getHeating());
            else stmt.setNull(12, Types.VARCHAR);
            if (row.getNumberOfRooms() != -1) stmt.setDouble(13, row.getNumberOfRooms());
            else stmt.setNull(13, Types.DOUBLE);
            if (row.getNumberOfToilets() != -1) stmt.setInt(14, row.getNumberOfToilets());
            else stmt.setNull(14, Types.INTEGER);
            if (row.hasParking()) stmt.setInt(15, 1);
            else stmt.setNull(15, Types.TINYINT);
            if (row.HasElevator()) stmt.setInt(16, 1);
            else stmt.setNull(16, Types.TINYINT);
            if (row.HasTerrace()) stmt.setInt(17, 1);
            else stmt.setNull(17, Types.TINYINT);

            stmt.executeUpdate();
            counter++;
            System.out.println("Added "+counter+" rows to database so far");
        } catch (SQLException e) {
            System.err.println("Something bad happened "+e.toString());
        }
    }
}
