#!/usr/bin/python3
import argparse
import signal
import sys
import time

import melee
import random

from Game.create_all_genes import generate
from NEAT import Genome_manager
from NEAT.graph.visualise_genome import Graph

#  This example program demonstrates how to use the Melee API to run a console,
#   setup controllers, and send button presses over to a console

def check_port(value):
    ivalue = int(value)
    if ivalue < 1 or ivalue > 4:
        raise argparse.ArgumentTypeError("%s is an invalid controller port. \
                                         Must be 1, 2, 3, or 4." % value)
    return ivalue


parser = argparse.ArgumentParser(description='Example of libmelee in action')
parser.add_argument('--port', '-p', type=check_port,
                    help='The controller port (1-4) your AI will play on',
                    default=2)
parser.add_argument('--opponent', '-o', type=check_port,
                    help='The controller port (1-4) the opponent will play on',
                    default=1)
parser.add_argument('--debug', '-d', action='store_true',
                    help='Debug mode. Creates a CSV of all game states')
parser.add_argument('--address', '-a', default="127.0.0.1",
                    help='IP address of Slippi/Wii')
parser.add_argument('--dolphin_executable_path', '-e', default=None,
                    help='The directory where dolphin is')
parser.add_argument('--connect_code', '-t', default="",
                    help='Direct connect code to connect to in Slippi Online')
parser.add_argument('--iso', default=None, type=str,
                    help='Path to melee iso.')

args = parser.parse_args()
print(args)

# This logger object is useful for retroactively debugging issues in your bot
#   You can write things to it each frame, and it will create a CSV file describing the match
log = None
if args.debug:
    log = melee.Logger()

# Create our Console object.
#   This will be one of the primary objects that we will interface with.
#   The Console represents the virtual or hardware system Melee is playing on.
#   Through this object, we can get "GameState" objects per-frame so that your
#       bot can actually "see" what's happening in the game

console = melee.Console(path="/Users/alessio/Library/Application Support/Slippi Launcher/netplay/Slippi Dolphin.app",
                        slippi_address=args.address,
                        logger=log)

# Create our Controller object
#   The controller is the second primary object your bot will interact with
#   Your controller is your way of sending button presses to the game, whether
#   virtual or physical.
controller = melee.Controller(console=console,
                              port=1,
                              type=melee.ControllerType.STANDARD)

controller_opponent = melee.Controller(console=console,
                                       port=4,
                                       type=melee.ControllerType.STANDARD)


# This isn't necessary, but makes it so that Dolphin will get killed when you ^C
def signal_handler(sig, frame):
    console.stop()
    if args.debug:
        log.writelog()
        print("")  # because the ^C will be on the terminal
        print("Log file created: " + log.filename)
    print("Shutting down cleanly...")
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

# Run the console
console.run(iso_path=r'/Users/alessio/Super Smash Bros. Melee (USA) (En,Ja) (v1.02).iso')

# Connect to the console
print("Connecting to console...")
if not console.connect():
    print("ERROR: Failed to connect to the console.")
    sys.exit(-1)
print("Console connected")

# Plug our controller in
#   Due to how named pipes work, this has to come AFTER running dolphin
#   NOTE: If you're loading a movie file, don't connect the controller,
#   dolphin will hang waiting for input and never receive it
print("Connecting controller to console...")
if not controller.connect():
    print("ERROR: Failed to connect the controller.")
    sys.exit(-1)
print("Controller connected")
controller_opponent.connect()

costume = 0
framedata = melee.framedata.FrameData()

# ia stuff here
gene_manager = generate()
genome_manager = Genome_manager.GenomeManager()
genome_manager.create_genome(gene_manager, 5)
genome_manager.create_genome(gene_manager, 5)
genome_manager.create_genome(gene_manager, 5)
genome_manager.create_genome(gene_manager, 5)
genome_manager.create_genome(gene_manager, 5)
Graph().create_graph(genome_manager.genomes[0], gene_manager)

refreshed = True
frame=0
percentP1 = 0
percentP4 = 0
stockP1 = 4
stockP4 = 4
generation = 0

actualGenome = 0
bestScore = -999999
bestGenome = None
# Main loop
while True:
    # "step" to the next frame
    gamestate = console.step()
    if gamestate is None:
        continue

    # The console object keeps track of how long your bot is taking to process frames
    #   And can warn you if it's taking too long
    if console.processingtime * 1000 > 12:
        print("WARNING: Last frame took " + str(console.processingtime * 1000) + "ms to process.")

    # What menu are we in?
    if gamestate.menu_state in [melee.Menu.IN_GAME, melee.Menu.SUDDEN_DEATH]:
        if frame == 1:
            frame = 0
            controller.release_all()
        else:
            frame += 1
            refreshed = False
            gene_chosen = genome_manager.genomes[actualGenome].calculate(gamestate, controller)
            gene_chosen.behavior(controller)
        if gamestate.players[1].percent > percentP1:
            #print(f"percent p1 start: {genome_manager.genomes[actualGenome].score}")
            genome_manager.genomes[actualGenome].score -= gamestate.players[1].percent - percentP1
            percentP1 = gamestate.players[1].percent
            #print(f"percent p1 end: {genome_manager.genomes[actualGenome].score}")
        if gamestate.players[4].percent > percentP4:
            #print(f"percent p4 start: {genome_manager.genomes[actualGenome].score}")
            genome_manager.genomes[actualGenome].score += gamestate.players[4].percent - percentP4
            percentP4 = gamestate.players[4].percent
            #print(f"percent p4 end: {genome_manager.genomes[actualGenome].score}")
        if gamestate.players[1].stock < stockP1:
            #print(f"stock p1 start: {genome_manager.genomes[actualGenome].score}")
            genome_manager.genomes[actualGenome].score -= 500
            stockP1 = gamestate.players[1].stock
            percentP1 = 0
            #print(f"stock p1 end: {genome_manager.genomes[actualGenome].score}")
        if gamestate.players[4].stock < stockP4:
            #print(f"stock p4 start: {genome_manager.genomes[actualGenome].score}")
            genome_manager.genomes[actualGenome].score += 500
            stockP4 = gamestate.players[4].stock
            percentP4 = 0
            #print(f"stock p4 start: {genome_manager.genomes[actualGenome].score}")
        #genome_manager.genomes[actualGenome].score -= 0.01
    else:
        if not refreshed:
            percentP1 = 0
            percentP4 = 0
            stockP1 = 4
            stockP4 = 4
            if actualGenome < 4:
                print(f"Genome {actualGenome} of Generation {generation} has a score of {genome_manager.genomes[actualGenome].score}")
                if genome_manager.genomes[actualGenome].score > bestScore:
                    bestGenome = genome_manager.genomes[actualGenome]
                actualGenome+=1
            else:
                print(f"Génération {generation}: "
                      f"\nGenome 1: {genome_manager.genomes[0].score}"
                      f"\nGenome 2: {genome_manager.genomes[1].score}"
                      f"\nGenome 3: {genome_manager.genomes[2].score}"
                      f"\nGenome 4: {genome_manager.genomes[3].score}"
                      f"\nGenome 5: {genome_manager.genomes[4].score}")
                generation += 1
                bestGenome.mutate(10, 1)
                Graph().create_graph(bestGenome, gene_manager)
                for value in genome_manager.genomes:
                    if value != bestGenome:
                        genome_manager.genomes.remove(value)
                genome_manager.create_genome(gene_manager, 5)
                genome_manager.create_genome(gene_manager, 5)
                genome_manager.create_genome(gene_manager, 5)
                genome_manager.create_genome(gene_manager, 5)
                actualGenome = 0
                bestScore = -999999
                bestGenome = None
        refreshed = True
        melee.MenuHelper.menu_helper_simple(gamestate,
                                            controller,
                                            melee.Character.MARTH,
                                            melee.Stage.BATTLEFIELD,
                                            args.connect_code,
                                            autostart=False,
                                            swag=False)
        melee.MenuHelper.menu_helper_simple(gamestate,
                                            controller_opponent,
                                            melee.Character.MARTH,
                                            melee.Stage.BATTLEFIELD,
                                            args.connect_code,
                                            cpu_level=9,
                                            costume=costume,
                                            autostart=True,
                                            swag=False)


        # If we're not in game, don't log the frame
        if log:
            log.skipframe()
