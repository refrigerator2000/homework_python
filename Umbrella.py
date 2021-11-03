
  
import operator
import string

str = '“Несколько лет тому назад в одном из своих поместий жил старинный русский барин, Кирила Петрович Троекуров. Его богатство, знатный род и связи давали ему большой вес в губерниях, где находилось его имение.\
     Соседи рады были угождать малейшим его прихотям; губернские чиновники трепетали при его имени; Кирила Петрович принимал знаки подобострастия как надлежащую дань; дом его всегда был полон гостями, готовыми тешить его барскую праздность, разделяя шумные, а иногда и буйные его увеселения.\
         Никто не дерзал отказываться от его приглашения или в известные дни не являться с должным почтением в село Покровское. В домашнем быту Кирила Петрович выказывал все пороки человека необразованного.\
             Избалованный всем, что только окружало его, он привык давать полную волю всем порывам пылкого своего нрава и всем затеям довольно ограниченного ума. Несмотря на необыкновенную силу физических способностей, он раза два в неделю страдал от обжорства и каждый вечер бывал навеселе.\
                  В одном из флигелей его дома жили шестнадцать горничных, занимаясь рукоделиями, свойственными их полу. Окна во флигеле были загорожены деревянною решеткою; двери запирались замками, от коих ключи хранились у Кирила Петровича. Молодые затворницы в положенные часы сходили в сад и прогуливались под надзором двух старух.\
                       От времени до времени Кирила Петрович выдавал некоторых из них замуж, и новые поступали на их место. С крестьянами и дворовыми обходился он строго и своенравно; несмотря на то, они были ему преданы: они тщеславились богатством и славою своего господина и в свою очередь позволяли себе многое в отношении к их соседам, надеясь на его сильное покровительство.”'

s = str.split()


def Umbrella(BunchWords):
    result = []
    for word in BunchWords:
        NewWord = ''
        HasPMark = False
        for ch in string.punctuation:
            if ch in word:
                HasPMark = True
                pos = word.find(ch)
                if pos == len(word) - 1:
                    NewWord = word[:pos]
                else:
                    NewWord = word[:pos] + word[pos + 1:]
        if not HasPMark:
               NewWord = word
               result.append(NewWord.lower())
    return result
C = Umbrella(s)
def CountWords(words):
       Wordss = set(words)
       Wordsd = {}
       for word in Wordss:
              Wordsd[word] = words.count(word)
       return Wordsd

SC = sorted(CountWords(C).items(), key=lambda x : x[1], reverse=True)
L = list(SC)[:10]
for word, num in L:
    print(word, ': ', num)