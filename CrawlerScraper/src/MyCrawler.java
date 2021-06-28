import edu.uci.ics.crawler4j.crawler.Page;
import edu.uci.ics.crawler4j.crawler.WebCrawler;
import edu.uci.ics.crawler4j.parser.HtmlParseData;
import edu.uci.ics.crawler4j.url.WebURL;
import org.apache.commons.io.FileUtils;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.io.File;
import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.util.Set;
import java.util.regex.Pattern;

public class MyCrawler extends WebCrawler {

    private final static Pattern EXCLUSIONS
            = Pattern.compile(".*(\\.(css|js|xml|gif|jpg|png|mp3|mp4|zip|gz|pdf|ico))$");

    /**
     * This method receives two parameters. The first parameter is the page
     * in which we have discovered this new url and the second parameter is
     * the new url. You should implement this function to specify whether
     * the given url should be crawled or not (based on your crawling logic).
     * In this example, we are instructing the crawler to ignore urls that
     * have css, js, git, ... extensions and to only accept urls that start
     * with "https://www.ics.uci.edu/". In this case, we didn't need the
     * referringPage parameter to make the decision.
     */
    @Override
    public boolean shouldVisit(Page referringPage, WebURL url) {
        String urlString = url.getURL().toLowerCase();
        return !EXCLUSIONS.matcher(urlString).matches()
                && (urlString.startsWith("https://www.4zida.rs/prodaja-stanova")
                    || urlString.startsWith("https://www.4zida.rs/prodaja-kuca")
                    || urlString.startsWith("https://www.4zida.rs/izdavanje-stanova")
                    || urlString.startsWith("https://www.4zida.rs/izdavanje-kuca")
                    || urlString.startsWith("https://www.4zida.rs/prodaja/stanovi")
                    || urlString.startsWith("https://www.4zida.rs/prodaja/kuce")
                    || urlString.startsWith("https://www.4zida.rs/izdavanje/stanovi")
                    || urlString.startsWith("https://www.4zida.rs/izdavanje/kuce"));
    }
    /**
     * This function is called when a page is fetched and ready
     * to be processed by your program.
     */
    @Override
    public void visit(Page page) {
        String url = page.getWebURL().getURL();
        //System.out.println("Visited page "+url);
        //Controller.countVisited(url);
        if (page.getParseData() instanceof HtmlParseData) {
            HtmlParseData htmlParseData = (HtmlParseData) page.getParseData();
            String html = htmlParseData.getHtml();
            Document doc = Jsoup.parse(html);
            boolean sale = false;
            if ((sale = url.startsWith("https://www.4zida.rs/prodaja/")) || url.startsWith("https://www.4zida.rs/izdavanje/")) {
                Elements elements;
                if (sale){
                    elements = doc.getElementsByClass("info-items ng-star-inserted").first().children();
                } else {
                    elements = doc.getElementById("meta-data").children();
                }
                //System.out.println("br atributa :"+elements.size());
                AnnotatedRow row = new AnnotatedRow();
                row.setForSale(sale?1:0);
                if (url.startsWith("https://www.4zida.rs/prodaja/kuce") || url.startsWith("https://www.4zida.rs/izdavanje/kuce"))
                    row.setPropertyType(0);
                else
                    row.setPropertyType(1);
                for (Element element : elements) {
                    if (element.tagName().equals("div") && element.hasClass("info-item") && element.child(0).text().equals("Cena:")) {
                        row.setPrice(element.child(1).child(0).text());
                        //System.out.println("cena: " + row.getPrice());
                    }
                    else if (element.hasClass("meta-data-title")){
                        Elements temp;
                        if (!(temp = element.getElementsByClass("location")).isEmpty()){
                            row.setTotalLocation(temp.first().text());
                            //System.out.println(temp.first().text());
                        }
                    }
                    else if (element.tagName().equals("app-info-item")){
                        if (!element.getElementsByClass("value").isEmpty()){
                            String value;
                            value = element.getElementsByClass("value").first().text();
                            //System.out.println(element.attr("label")+": "+value);
                            row.setAttribute(element.attr("label"),value);

                        }
                    }

                }
                row.writeToDB();
            }

        }
    }
}