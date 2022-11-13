# generateur de Secret Santa pour le Forum Dessiné (en Python)

Tirage au chapeau d'un secret santa, en tenant compte des exclusions potentielles de chacun.es

# Necessite:

*  Python3


# Instructions

## 1. Download the repositorie

## 2. Modifiez le fichier de configuration

Faites les modifications que vous souhaitez dans le fichier 'config.py'.

Dans ce dernier, vous devez indiquer:

*  La liste des secrets santas.
*  Leurs souhaits
*  Les exclusions éventuelles de chacun.es.

## 3. Testez le script

## 4. Ouvrz le fichier 'send-letters.py'


This will read the configuration file and perform a "dry run" of the various
pairings between secret Santas and recipients. It will generate an output file
as specified by the `record_file` setting in `config.py` (by default
it is `secret-santa-email-record.txt`).


## 5. ùenvoyez les messages privés via la messagerie du Forum Dessiné
copiez-collez les paragraphes dans le .txt ainsi généré. Envoyez les à chaque participantes via la messagerie interne du Forum Dessiné
