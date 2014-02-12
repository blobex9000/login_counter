class TestapiController < ApplicationController

  def resetFixture
   begin
      #puts "blahblahblah"
      User.TESTAPI_resetFixture
      msg = { :errCode => 1 }
      render :status => 200, :json => msg 
    rescue Exception => e
      render :nothing => true, :status => 500
    end    
  end

  def unitTests
    #begin
      puts "happy happy joy joy"
      `rake test test/models/user_test.rb > tmp/unit_test_results.out`
      uTestsResults = `cat tmp/unit_test_results.out`
      #adfsdf
      numTestsAndFailedLine = `cat tmp/unit_test_results.out | grep '[0-9]* failures'`
      #uTestResults = numTestsAndFailedLine
      failedSplitString = numTestsAndFailedLine.split(" failures").first
      testsSplitString = numTestsAndFailedLine.split(" tests").first
      numFailed = failedSplitString.split(" ").last.to_i
      numTests = testsSplitString.split(" ").last.to_i
      msg = { :nrFailed => numFailed, :output => uTestsResults, :totalTests => numTests }
      render :status => 200, :json => msg
    #rescue  Exception => e
    #  uTestsResults = `cat tmp/unit_test_results.out`
    #  msg = { :output => uTestsResults }
    #  render :status => 500, :json => msg
    #end
  end

end
