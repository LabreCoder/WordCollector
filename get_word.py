import requests
import random

def get_random_word():
    url = "https://random-word-api.herokuapp.com/word"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()[0]

    except requests.exceptions.Timeout:
        return None  # timeout explícito

    except requests.exceptions.HTTPError:
        return None  # erro HTTP (4xx / 5xx)

    except requests.exceptions.RequestException:
        return None  # qualquer outro erro de rede
    
def get_word():

    random.seed()
    words = [
        # 1–10
        "ability","absence","academy","account","accuracy","achievement","activity","addition","address","adjustment",
        # 11–20
        "admission","advantage","adventure","advertising","agreement","aircraft","analysis","announcement","anxiety","apartment",
        # 21–30
        "appearance","application","appointment","argument","arrival","assistant","atmosphere","attachment","attempt","attention",
        # 31–40
        "attitude","audience","authority","awareness","background","balance","barrier","behavior","benefit","boundary",
        # 41–50
        "breakfast","building","business","calendar","campaign","capacity","category","celebration","challenge","character",
        # 51–60
        "chemistry","childhood","circumstance","citizenship","classroom","collection","committee","community","comparison","competition",
        # 61–70
        "complaint","completion","complexity","component","confidence","conflict","connection","consequence","consideration","construction",
        # 71–80
        "consultation","contribution","conversation","cooperation","coordination","creativity","credibility","criticism","curiosity","customer",
        # 81–90
        "database","decision","definition","delivery","democracy","department","description","development","difference","difficulty",
        # 91–100
        "direction","disaster","discipline","discussion","distribution","education","efficiency","electricity","emergency","employment",

        # 101–110
        "encouragement","engineering","entertainment","environment","equipment","evaluation","examination","experience","experiment","explanation",
        # 111–120
        "expression","extension","facility","failure","foundation","freedom","frequency","friendship","function","generation",
        # 121–130
        "government","guidance","happiness","hardware","headline","healthcare","historian","household","hypothesis","identity",
        # 131–140
        "imagination","implementation","importance","improvement","independence","information","initiative","innovation","inspection","instruction",
        # 141–150
        "integration","intelligence","interaction","investment","knowledge","leadership","legislation","literature","management","measurement",
        # 151–160
        "mechanism","membership","migration","motivation","navigation","negotiation","networking","obligation","observation","operation",
        # 161–170
        "opportunity","organization","orientation","ownership","participation","performance","permission","personality","perspective","philosophy",
        # 171–180
        "platform","pollution","population","possibility","prediction","preparation","presentation","priority","probability","procedure",

        # 181–190
        "productivity","profession","protection","psychology","publication","qualification","questionnaire","recognition","recommendation","reflection",
        # 191–200
        "regulation","relationship","reliability","replacement","representation","requirement","reservation","resolution","responsibility","restoration",
        # 201–210
        "revolution","satisfaction","scholarship","scientist","selection","sensitivity","separation","significance","simulation","situation",
        # 211–220
        "society","software","solution","specification","strategy","structure","substance","supervision","sustainability","technology",
        # 221–230
        "temperature","theory","threshold","tradition","transformation","translation","transportation","understanding","university","validation",
        # 231–240
        "variation","vegetation","verification","vocabulary","volunteer","vulnerability","willingness","workforce","workplace","achievementism",

        # 241–250
        "adaptation","alignment","allocation","ambition","amplification","anticipation","authentication","automation","benchmark","calculation",
        # 251–260
        "collaboration","compression","configuration","consolidation","constraint","consumption","context","correlation","customization","debugging",
        # 261–270
        "declaration","decomposition","dedication","dependency","deployment","diagnostics","differentiation","digitalization","disruption","documentation",
        # 271–280
        "encryption","enhancement","estimation","exploration","fabrication","forecasting","formalization","globalization","harmonization","identification",
        # 281–290
        "illumination","implementationism","indexation","industrialization","initialization","instrumentation","interoperability","localization","mobilization","modernization",

        # 291–300
        "normalization","optimization","orchestration","parameterization","prioritization","quantification","rationalization","reconfiguration","refactoring","regression",
        # 301–310
        "reinforcement","replication","scheduling","serialization","simplification","synchronization","tokenization","transmission","utilization","virtualization",
        # 311–320
        "accessibility","accountability","adaptability","affordability","authenticity","compatibility","confidentiality","connectivity","consistency","durability",
        # 321–330
        "elasticity","extensibility","flexibility","interactivity","maintainability","observability","portability","recoverability","scalability","traceability",

        # 331–340
        "acceptance","acquisition","activation","aggregation","annotation","approximation","assimilation","categorization","classification","codification",
        # 341–350
        "computation","conceptualization","contextualization","decentralization","delimitation","derivation","disambiguation","enumeration","formalism","generalization",
        # 351–360
        "granularity","hierarchy","idealization","instantiation","interpretation","iteration","linearization","materialization","modularization","objectification",

        # 361–370
        "parameter","randomization","reduction","segmentation","standardization","symbolization","taxonomy","thematization","typification","validationism",
        # 371–380
        "aggregationism","classificationism","formalizationism","generalism","individualism","materialism","mechanism","naturalism","pragmatism","structuralism",

        # 381–390
        "abstraction","algorithm","bandwidth","bitrate","compiler","container","cybersecurity","datagram","encryptionism","firewall",
        # 391–400
        "firmware","framework","handshake","hashing","hypervisor","infrastructure","latency","middleware","microservice","packet",

        # 401–410
        "protocol","redundancy","repository","sandbox","scanning","scheduler","throughput","topology","virtualmachine","workload",

        # 411–420
        "analysisism","automationism","configurationism","deploymentism","monitoring","observabilityism","optimizationism","provisioning","resilience","telemetry",

        # 421–430
        "alerting","auditing","backup","balancing","caching","clustering","containerization","hardening","loadtesting","logging",

        # 431–440
        "patching","profiling","provisioningism","replicationism","scaling","snapshot","throttling","tuning","versioning","watchdog",

        # 441–450
        "adapter","broker","client","daemon","endpoint","gateway","listener","publisher","subscriber","worker",

        # 451–460
        "accuracyism","availability","completeness","consensus","consistencyism","durabilityism","fairness","integrity","isolation","reliabilityism",

        # 461–470
        "timestamp","checksum","nonce","payload","signature","certificate","authorityism","authenticationism","authorization","confidentialityism",

        # 471–480
        "accounting","billing","charging","forecast","inventory","licensing","procurement","reporting","revenue","subscription",

        # 481–490
        "benchmarking","compliance","governance","mitigation","policy","riskassessment","roadmap","stakeholder","strategyism","vision",

        # 491–500
        "alignmentism","culture","diversity","equity","inclusion","leadershipism","mentorship","ownershipism","performanceism","transparency",
    ]

    return random.choice(words)