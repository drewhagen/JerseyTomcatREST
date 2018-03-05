package csv_data_analysis;

/*import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVParser;
import org.apache.commons.csv.CSVRecord;*/

import java.io.IOException;
import java.io.Reader;
import java.nio.file.Files;
import java.nio.file.Paths;

public class CSVsample {

    private static final String csvPath = "/../../resources/csv_files";

    public static void main(String[] args) throws IOException {
        /*try (
                Reader reader = Files.newBufferedReader(Paths.get(csvPath));
                CSVParser csvParser = new CSVParser(reader, CSVFormat.DEFAULT
                        .withHeader("name", "email", "phone", "country")
                        .withIgnoreHeaderCase()
                        .withTrim());
        ) {
            for (CSVRecord csvRecord : csvParser.getRecords()) {
                // Accessing values by the names assigned to each column

                String name = csvRecord.get("Name");
                String email = csvRecord.get("Email");
                String phone = csvRecord.get("Phone");
                String country = csvRecord.get("Country");

                System.out.println("Record No - " + csvRecord.getRecordNumber());
                System.out.println("---------------");
                System.out.println("Name : " + name);
                System.out.println("Email : " + email);
                System.out.println("Phone : " + phone);
                System.out.println("Country : " + country);
                System.out.println("---------------\n\n");
            }
        }*/
    }
}
