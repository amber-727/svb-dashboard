import requests
from bs4 import BeautifulSoup
import csv
import time
import sys

URLS = [
    "https://www.svb.com/profile/abbey-honegger/",
    "https://www.svb.com/profile/adam-gervais/",
    "https://www.svb.com/profile/adam-graham/",
    "https://www.svb.com/profile/adam-tweedy/",
    "https://www.svb.com/profile/alan-nguyen/",
    "https://www.svb.com/profile/alexander-addario/",
    "https://www.svb.com/profile/alexandra-marshall/",
    "https://www.svb.com/profile/alex-lennox-miller/",
    "https://www.svb.com/profile/alicia-fuller/",
    "https://www.svb.com/profile/amanda-kent/",
    "https://www.svb.com/profile/amy-rowe/",
    "https://www.svb.com/profile/andrea-hernandez/",
    "https://www.svb.com/profile/andrew-mccarty/",
    "https://www.svb.com/profile/andrew-pardo/",
    "https://www.svb.com/profile/andrew-rossillon/",
    "https://www.svb.com/profile/andy-tsao/",
    "https://www.svb.com/profile/angela-sellers/",
    "https://www.svb.com/profile/anna-cade/",
    "https://www.svb.com/profile/annie-chiu/",
    "https://www.svb.com/profile/anthony-vassallo/",
    "https://www.svb.com/profile/arianne-perry/",
    "https://www.svb.com/profile/armando-a-argueta/",
    "https://www.svb.com/profile/barnaby-chery/",
    "https://www.svb.com/profile/ben-johnston/",
    "https://www.svb.com/profile/bill-sideris/",
    "https://www.svb.com/profile/blake-armstrong/",
    "https://www.svb.com/profile/blake-lepire/",
    "https://www.svb.com/profile/bobby-donnelly/",
    "https://www.svb.com/profile/bo-ren/",
    "https://www.svb.com/profile/brenda-santoro/",
    "https://www.svb.com/profile/bret-turner/",
    "https://www.svb.com/profile/brian-brown/",
    "https://www.svb.com/profile/brian-foley/",
    "https://www.svb.com/profile/brian-kass/",
    "https://www.svb.com/profile/brian-lowry/",
    "https://www.svb.com/profile/brian-mcguire/",
    "https://www.svb.com/profile/brian-sherer/",
    "https://www.svb.com/profile/brian-taylor/",
    "https://www.svb.com/profile/bruce-helberg/",
    "https://www.svb.com/profile/bryan-brenchley/",
    "https://www.svb.com/profile/caitlin-cloud/",
    "https://www.svb.com/profile/calvert-wong/",
    "https://www.svb.com/profile/carla-winfield/",
    "https://www.svb.com/profile/carmela-montes-de-oca/",
    "https://www.svb.com/profile/carmen-sudhausen/",
    "https://www.svb.com/profile/carrie-merritt/",
    "https://www.svb.com/profile/chandler-white/",
    "https://www.svb.com/profile/chelsea-hakso/",
    "https://www.svb.com/profile/cheryl-day/",
    "https://www.svb.com/profile/chris-canazaro/",
    "https://www.svb.com/profile/chris-leary/",
    "https://www.svb.com/profile/chris-stoecker/",
    "https://www.svb.com/profile/christi-fletcher/",
    "https://www.svb.com/profile/christina-bertram/",
    "https://www.svb.com/profile/cindy-schatz/",
    "https://www.svb.com/profile/cj-bradford/",
    "https://www.svb.com/profile/claudia-canales/",
    "https://www.svb.com/profile/craig-smith/",
    "https://www.svb.com/profile/cynthia-brooks-manson/",
    "https://www.svb.com/profile/dan-baldi/",
    "https://www.svb.com/profile/daniel-dehrey/",
    "https://www.svb.com/profile/danielle-conkling/",
    "https://www.svb.com/profile/danny-donovan/",
    "https://www.svb.com/profile/darrell-leong/",
    "https://www.svb.com/profile/david-song/",
    "https://www.svb.com/profile/dawn-mcfadden/",
    "https://www.svb.com/profile/dax-williamson/",
    "https://www.svb.com/profile/debi-kutaka/",
    "https://www.svb.com/profile/dennis-brown/",
    "https://www.svb.com/profile/dennis-flaherty/",
    "https://www.svb.com/profile/dennis-grunt/",
    "https://www.svb.com/profile/dennis-he/",
    "https://www.svb.com/profile/dennis-rapoport/",
    "https://www.svb.com/profile/diane-dodge-bianchini/",
    "https://www.svb.com/profile/dirk-engelbert/",
    "https://www.svb.com/profile/dylan-wong/",
    "https://www.svb.com/profile/edward-lee/",
    "https://www.svb.com/profile/elias-saadeh/",
    "https://www.svb.com/profile/eli-oftedal/",
    "https://www.svb.com/profile/ella-katrina-clark/",
    "https://www.svb.com/profile/emily-gonsenheim/",
    "https://www.svb.com/profile/emily-nguyen/",
    "https://www.svb.com/profile/emma-eschweiler/",
    "https://www.svb.com/profile/erica-douvadjian/",
    "https://www.svb.com/profile/eric-otterson/",
    "https://www.svb.com/profile/esha-bawa/",
    "https://www.svb.com/profile/estefania-cunha-flynn/",
    "https://www.svb.com/profile/evelyn-sainato/",
    "https://www.svb.com/profile/faisal-mostamandy/",
    "https://www.svb.com/profile/fiona-hsu/",
    "https://www.svb.com/profile/francis-bonnemere/",
    "https://www.svb.com/profile/frank-o-brien/",
    "https://www.svb.com/profile/garrett-hoemmen/",
    "https://www.svb.com/profile/gary-jackson/",
    "https://www.svb.com/profile/gerald-brady/",
    "https://www.svb.com/profile/glen-mello/",
    "https://www.svb.com/profile/greg-gregory/",
    "https://www.svb.com/profile/greg-sarhanis/",
    "https://www.svb.com/profile/heather-giles/",
    "https://www.svb.com/profile/hiroshi-ikemoto/",
    "https://www.svb.com/profile/ilana-fass/",
    "https://www.svb.com/profile/ireland-carter/",
    "https://www.svb.com/profile/irwin-bautista/",
    "https://www.svb.com/profile/ivan-asensio/",
    "https://www.svb.com/profile/jack-garza/",
    "https://www.svb.com/profile/jack-gaziano/",
    "https://www.svb.com/profile/jake-ledbetter/",
    "https://www.svb.com/profile/janet-zamudio/",
    "https://www.svb.com/profile/jason-cosso/",
    "https://www.svb.com/profile/jason-graveley/",
    "https://www.svb.com/profile/jeannette-roy/",
    "https://www.svb.com/profile/jed-taborski/",
    "https://www.svb.com/profile/jenna-odonnell/",
    "https://www.svb.com/profile/jennifer-friel-goldstein/",
    "https://www.svb.com/profile/jenni-halleran/",
    "https://www.svb.com/profile/jeremy-rich/",
    "https://www.svb.com/profile/jesse-hurley/",
    "https://www.svb.com/profile/jessica-harris/",
    "https://www.svb.com/profile/joanne-hoang/",
    "https://www.svb.com/profile/joe-brigati/",
    "https://www.svb.com/profile/john-lee/",
    "https://www.svb.com/profile/john-schweizer/",
    "https://www.svb.com/profile/john-topolosky/",
    "https://www.svb.com/profile/jolinda-gladstein/",
    "https://www.svb.com/profile/jon-schwartz/",
    "https://www.svb.com/profile/jordan-kanis/",
    "https://www.svb.com/profile/jordan-parcell/",
    "https://www.svb.com/profile/joseph-smart/",
    "https://www.svb.com/profile/jose-sevilla/",
    "https://www.svb.com/profile/Josh-Pherigo/",
    "https://www.svb.com/profile/jp-giannini/",
    "https://www.svb.com/profile/julia-bobrovich/",
    "https://www.svb.com/profile/julian-nash/",
    "https://www.svb.com/profile/julie-wagne/",
    "https://www.svb.com/profile/justine-nguyen/",
    "https://www.svb.com/profile/justin-mauch/",
    "https://www.svb.com/profile/kadie-sobel/",
    "https://www.svb.com/profile/kaitlin-berube/",
    "https://www.svb.com/profile/karen-toste/",
    "https://www.svb.com/profile/kathy-sun/",
    "https://www.svb.com/profile/katie-ratliff/",
    "https://www.svb.com/profile/kelley-henry/",
    "https://www.svb.com/profile/kevin-conway/",
    "https://www.svb.com/profile/kevin-li/",
    "https://www.svb.com/profile/kevin-scott/",
    "https://www.svb.com/profile/kim-dalpe/",
    "https://www.svb.com/profile/kiran-malhotra/",
    "https://www.svb.com/profile/krista-estep/",
    "https://www.svb.com/profile/kyle-kistner/",
    "https://www.svb.com/profile/kyle-larrabee/",
    "https://www.svb.com/profile/lafe-vittitoe/",
    "https://www.svb.com/profile/lane-bruno/",
    "https://www.svb.com/profile/larry-zahn/",
    "https://www.svb.com/profile/laura-scott/",
    "https://www.svb.com/profile/lauren-rasch-morrell/",
    "https://www.svb.com/profile/leslie-cowan/",
    "https://www.svb.com/profile/liam-fairbairn/",
    "https://www.svb.com/profile/lily-page/",
    "https://www.svb.com/profile/linda-nguyen/",
    "https://www.svb.com/profile/lisa-treshnell/",
    "https://www.svb.com/profile/lisa-wei-goel/",
    "https://www.svb.com/profile/li-song/",
    "https://www.svb.com/profile/liz-stokka/",
    "https://www.svb.com/profile/luena-lamani/",
    "https://www.svb.com/profile/mandi-paul/",
    "https://www.svb.com/profile/marc-c-cadieux/",
    "https://www.svb.com/profile/marc-neri/",
    "https://www.svb.com/profile/marisa-mathews/",
    "https://www.svb.com/profile/marisa-phan/",
    "https://www.svb.com/profile/mark-freund/",
    "https://www.svb.com/profile/mark-gallagher/",
    "https://www.svb.com/profile/mark-harris/",
    "https://www.svb.com/profile/mark-lau/",
    "https://www.svb.com/profile/mark-noble/",
    "https://www.svb.com/profile/mark-peterson/",
    "https://www.svb.com/profile/mark-thylin/",
    "https://www.svb.com/profile/marshall-graves/",
    "https://www.svb.com/profile/matthew-reiswig/",
    "https://www.svb.com/profile/matthew-wright/",
    "https://www.svb.com/profile/max-froseth/",
    "https://www.svb.com/profile/megan-scheffel/",
    "https://www.svb.com/profile/meghan-hynes/",
    "https://www.svb.com/profile/mei-chui/",
    "https://www.svb.com/profile/mei-theng/",
    "https://www.svb.com/profile/micaela-amaroli/",
    "https://www.svb.com/profile/michael-duranceau/",
    "https://www.svb.com/profile/michael-fell/",
    "https://www.svb.com/profile/michael-ritter/",
    "https://www.svb.com/profile/mike-devery/",
    "https://www.svb.com/profile/mike-ingoglia/",
    "https://www.svb.com/profile/mike-tramack/",
    "https://www.svb.com/profile/minh-trang/",
    "https://www.svb.com/profile/miranda-jimenez-fajardo/",
    "https://www.svb.com/profile/mona-maitra/",
    "https://www.svb.com/profile/nanci-fastre/",
    "https://www.svb.com/profile/nancy-trieu/",
    "https://www.svb.com/profile/natalie-fratto/",
    "https://www.svb.com/profile/natalie-steck/",
    "https://www.svb.com/profile/nate-foley/",
    "https://www.svb.com/profile/nathan-morrell/",
    "https://www.svb.com/profile/nicholas-drapeau/",
    "https://www.svb.com/profile/nicholas-farguson/",
    "https://www.svb.com/profile/nick-christian/",
    "https://www.svb.com/profile/nick-french/",
    "https://www.svb.com/profile/nick-wolfe/",
    "https://www.svb.com/profile/nicole-hawkey/",
    "https://www.svb.com/profile/nina-kandilian/",
    "https://www.svb.com/profile/nixon-jaquez/",
    "https://www.svb.com/profile/pamella-benac/",
    "https://www.svb.com/profile/parnaz-partowkia/",
    "https://www.svb.com/profile/patrick-haggerty/",
    "https://www.svb.com/profile/patty-kao/",
    "https://www.svb.com/profile/paul-cominsky/",
    "https://www.svb.com/profile/peter-compton/",
    "https://www.svb.com/profile/peter-freyer/",
    "https://www.svb.com/profile/phil-silvia/",
    "https://www.svb.com/profile/renuka-kumar/",
    "https://www.svb.com/profile/rob-derry/",
    "https://www.svb.com/profile/robert-mingrone/",
    "https://www.svb.com/profile/robert-o-connor/",
    "https://www.svb.com/profile/robert-sureck/",
    "https://www.svb.com/profile/robert-wood/",
    "https://www.svb.com/profile/rob-helm/",
    "https://www.svb.com/profile/robin-gill/",
    "https://www.svb.com/profile/rob-mcmillan/",
    "https://www.svb.com/profile/rob-walker/",
    "https://www.svb.com/profile/rob-zerby/",
    "https://www.svb.com/profile/rona-smith/",
    "https://www.svb.com/profile/roxana-palacios/",
    "https://www.svb.com/profile/samantha-colletti/",
    "https://www.svb.com/profile/sapna-easwar/",
    "https://www.svb.com/profile/sarah-he/",
    "https://www.svb.com/profile/sarah-kudrikow/",
    "https://www.svb.com/profile/sara-mclaughlin/",
    "https://www.svb.com/profile/sara-rona/",
    "https://www.svb.com/profile/scott-mccarty/",
    "https://www.svb.com/profile/scott-middleton/",
    "https://www.svb.com/profile/sean-stone/",
    "https://www.svb.com/profile/shane-anderson/",
    "https://www.svb.com/profile/shane-anderson2/",
    "https://www.svb.com/profile/sharon-marichalar/",
    "https://www.svb.com/profile/shawn-repulles/",
    "https://www.svb.com/profile/simon-keyes/",
    "https://www.svb.com/profile/stephanie-sier/",
    "https://www.svb.com/profile/steve-johnson/",
    "https://www.svb.com/profile/steven-jo/",
    "https://www.svb.com/profile/steven-mazovetskiy/",
    "https://www.svb.com/profile/steven-reel/",
    "https://www.svb.com/profile/suzann-russell/",
    "https://www.svb.com/profile/thomas-powley/",
    "https://www.svb.com/profile/timothy-a-lee/",
    "https://www.svb.com/profile/tim-bulakul/",
    "https://www.svb.com/profile/tim-walsh/",
    "https://www.svb.com/profile/tina-tran/",
    "https://www.svb.com/profile/tina-yim-cheung/",
    "https://www.svb.com/profile/todd-brothers/",
    "https://www.svb.com/profile/tom-gordon/",
    "https://www.svb.com/profile/tony-vicari/",
    "https://www.svb.com/profile/tosh-ernest/",
    "https://www.svb.com/profile/travis-dugan/",
    "https://www.svb.com/profile/trent-gordon/",
    "https://www.svb.com/profile/troy-ault/",
    "https://www.svb.com/profile/tyler-dean/",
    "https://www.svb.com/profile/tyler-dietrich/",
    "https://www.svb.com/profile/tyler-dittrich/",
    "https://www.svb.com/profile/vera-shokina/",
    "https://www.svb.com/profile/verina-hanien/",
    "https://www.svb.com/profile/wibke-pendse/",
    "https://www.svb.com/profile/william-sealy/",
    "https://www.svb.com/profile/will-joyce/",
]

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}


def scrape_profile(url: str) -> dict:
    try:
        resp = requests.get(url, headers=HEADERS, timeout=15)
        resp.raise_for_status()
    except Exception as e:
        print(f"  ERROR fetching {url}: {e}", file=sys.stderr)
        return {"url": url, "name": "", "title": "", "team": "", "location": ""}

    soup = BeautifulSoup(resp.text, "html.parser")

    def get(selector, attr=None):
        el = soup.select_one(selector)
        if not el:
            return ""
        return (el.get(attr) or "").strip() if attr else el.get_text(strip=True)

    # Name: schema.org itemprop on the h1
    name = get('h1[itemprop="name"]') or get("h1")

    # Title: appears in a div with class "h5 bold"; also parse from <title> tag as fallback
    title = get("div.h5.bold")
    if not title:
        page_title = soup.title.get_text(strip=True) if soup.title else ""
        if " - " in page_title:
            title = page_title.split(" - ", 1)[1]

    # Team / department: schema.org worksFor
    team = get('span[itemprop="worksFor"]')

    # Location: schema.org workLocation (the span, not the anchor)
    loc_el = soup.select_one('span[itemprop="workLocation"]')
    location = loc_el.get_text(strip=True) if loc_el else ""

    return {
        "url": url,
        "name": name,
        "title": title,
        "team": team,
        "location": location,
    }


def main():
    output_path = "/Users/amberhearn/svb-dashboard/svb-employees.csv"
    results = []
    total = len(URLS)

    for i, url in enumerate(URLS, 1):
        print(f"[{i}/{total}] {url}")
        data = scrape_profile(url)
        results.append(data)
        print(f"       name={data['name']!r}  title={data['title']!r}  team={data['team']!r}  loc={data['location']!r}")
        time.sleep(0.4)  # polite crawl delay

    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "title", "team", "location", "url"])
        writer.writeheader()
        writer.writerows(results)

    found = sum(1 for r in results if r["name"])
    print(f"\nDone. {found}/{total} profiles extracted. Saved to {output_path}")


if __name__ == "__main__":
    main()
