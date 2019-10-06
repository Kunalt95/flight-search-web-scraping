require 'test_helper'

class FlightControllerTest < ActionDispatch::IntegrationTest
  test "should get index" do
    get flight_index_url
    assert_response :success
  end

end
