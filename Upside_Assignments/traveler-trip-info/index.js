'use strict';

// TODO Import what you need
var airlinesService = require('./api/airlines.service') 
var profilesService = require('./api/profiles.service') 
var tripService = require('./api/trip.service')

function getTravelersFlightInfo() {

  // TODO Replace this hard coded response with your code
  let travelers=[];
  let travelersArray = Promise.all([airlinesService.get(), profilesService.get(), tripService.get()])
    .then(([airlines, profiles, trip]) => {
      trip.trip.flights.map(index => {
        index.travelerIds.map(travelerId => {
          if(travelers.some(traveler => traveler.id === travelerId)){
            travelers.map(traveler => {
              if(traveler.id === travelerId){
                traveler.flights.push({
                    legs: 
                      index.legs.map(index => {return  {
                        airlineCode: index.airlineCode,
                        airlineName: airlines.airlines.filter(airlineName => {return airlineName.code === index.airlineCode})[0]['name'],
                        flightNumber: index.flightNumber,
                        frequentFlyerNumber: profiles.profiles.filter(profile => {return profile.personId === travelerId})[0]?.rewardPrograms?.air?.[index.airlineCode] ?? ''
                      }})
                    },
                  )
                }
              })    
          }else{
            travelers.push({
              id: travelerId,
              name: profiles.profiles.filter(travelerName => {return travelerName.personId === travelerId})[0]['name'],
              flights: [
                {legs: 
                  index.legs.map(index => {return  {
                    airlineCode: index.airlineCode,
                    airlineName: airlines.airlines.filter(airlineName => {return airlineName.code === index.airlineCode})[0]['name'],
                    flightNumber: index.flightNumber,
                    frequentFlyerNumber: profiles.profiles.filter(profile => {return profile.personId === travelerId})[0]?.rewardPrograms?.air?.[index.airlineCode] ?? ''
                  }})
                },
              ],
            })
          }
        })
      })

      return {travelers : travelers}

    }).catch(err => console.log(err));

  return Promise.resolve(travelersArray) ;
}

module.exports = getTravelersFlightInfo;

/**For Tests purposes */
//const util = require('util')
//getTravelersFlightInfo().then(res => console.log(util.inspect(res, {showHidden: false, depth: null})))
