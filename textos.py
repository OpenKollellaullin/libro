# ejemplo para la manipulacion de textos

# variables con comillas simples
sitio = 'www.python.or'
print sitio

# variables con comillas dobles
sitio = "www.python.or"
print sitio

# variables multilineas

banner = """
        _________         ___.                                                      
\_   ___ \ ___.__.\_ |__    ____ _______                                    
/    \  \/<   |  | | __ \ _/ __ \\_  __ \                                   
\     \____\___  | | \_\ \\  ___/ |  | \/                                   
 \______  // ____| |___  / \___  >|__|                                      
        \/ \/          \/      \/                                           
  _________                              .__   __                           
 /   _____/  ____   ____   __ __ _______ |__|_/  |_  ___.__.                
 \_____  \ _/ __ \_/ ___\ |  |  \\_  __ \|  |\   __\<   |  |                
 /        \\  ___/\  \___ |  |  / |  | \/|  | |  |   \___  |                
/_______  / \___  >\___  >|____/  |__|   |__| |__|   / ____|                
        \/      \/     \/                            \/                     
.____            ___.                            __                         
|    |    _____  \_ |__    ____ _______ _____  _/  |_  ____ _______  ___.__.
|    |    \__  \  | __ \  /  _ \\_  __ \\__  \ \   __\/  _ \\_  __ \<   |  |
|    |___  / __ \_| \_\ \(  <_> )|  | \/ / __ \_|  | (  <_> )|  | \/ \___  |
|_______ \(____  /|___  / \____/ |__|   (____  /|__|  \____/ |__|    / ____|
        \/     \/     \/                     \/                      \/     
        """
print banner

# contar caracteres 

sitio = "https://www.python.org"
print len(sitio)

# concatenacion con signo +
protocolo = "https://"
sitio = "www.python.org"
print protocolo + sitio

# concatenacion con signo ,
protocolo = "https://"
sitio = "www.python.org"
print protocolo , sitio

# interpolacion 
protocolo = "https://"
sitio = "www.python.org"
print "el protocolo usado es {0} y el dominio es {1} ".format(protocolo,sitio)
