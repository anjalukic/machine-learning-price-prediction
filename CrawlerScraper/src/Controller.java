import edu.uci.ics.crawler4j.crawler.CrawlConfig;
import edu.uci.ics.crawler4j.crawler.CrawlController;
import edu.uci.ics.crawler4j.fetcher.PageFetcher;
import edu.uci.ics.crawler4j.robotstxt.RobotstxtConfig;
import edu.uci.ics.crawler4j.robotstxt.RobotstxtServer;

public class Controller {
    private static int aptSaleCount;
    private static  int houseSaleCount;
    private static  int aptSubletCount;
    private static  int houseSubletCount;

    public static void main(String[] args) throws Exception {
        String crawlStorageFolder = "src/data/crawl/root";
        int numberOfCrawlers = 7;

        Database.initialize();
        CrawlConfig config = new CrawlConfig();
        config.setCrawlStorageFolder(crawlStorageFolder);
        //config.setMaxDepthOfCrawling(1);
        config.setUserAgentString("Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0");

       // config.setIncludeHttpsPages(true);

        // Instantiate the controller for this crawl.
        PageFetcher pageFetcher = new PageFetcher(config);
        RobotstxtConfig robotstxtConfig = new RobotstxtConfig();
        RobotstxtServer robotstxtServer = new RobotstxtServer(robotstxtConfig, pageFetcher);
        CrawlController controller = new CrawlController(config, pageFetcher, robotstxtServer);

        // For each crawl, you need to add some seed urls. These are the first
        // URLs that are fetched and then the crawler starts following links
        // which are found in these pages
        controller.addSeed("https://www.4zida.rs/prodaja-stanova");
        controller.addSeed("https://www.4zida.rs/prodaja-kuca");
        controller.addSeed("https://www.4zida.rs/izdavanje-stanova");
        controller.addSeed("https://www.4zida.rs/izdavanje-kuca");
        //controller.addSeed("https://www.4zida.rs/izdavanje/stanovi/nis/oglas/sojka/60b74a26e0b31846c52837d8");

        // The factory which creates instances of crawlers.
        CrawlController.WebCrawlerFactory<MyCrawler> factory = MyCrawler::new;

        // Start the crawl. This is a blocking operation, meaning that your code
        // will reach the line after this only when crawling is finished.
        controller.start(factory, numberOfCrawlers);
    }

    public static void countVisited(String url){
        if (url.startsWith("https://www.4zida.rs/prodaja/stanovi"))
            aptSaleCount++;
        else if (url.startsWith("https://www.4zida.rs/prodaja/kuce"))
            houseSaleCount++;
        else if (url.startsWith("https://www.4zida.rs/izdavanje/stanovi"))
            aptSubletCount++;
        else if (url.startsWith("https://www.4zida.rs/izdavanje/kuce"))
            houseSubletCount++;
        System.out.println("\n----------------------------------------------------Sublet apts : "+aptSubletCount);
        System.out.println("\n----------------------------------------------------Sublet houses : "+houseSubletCount);
        System.out.println("\n----------------------------------------------------Sale apts : "+aptSaleCount);
        System.out.println("\n----------------------------------------------------Sale houses : "+houseSaleCount+"\n");

    }
}