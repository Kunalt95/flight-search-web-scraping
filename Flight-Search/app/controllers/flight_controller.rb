class FlightController < ApplicationController
  def index
    @flights = CheapFlights.all
  end
end
