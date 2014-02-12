require 'test_helper'

class UserTest < ActiveSupport::TestCase

  SUCCESS = 1
  ERR_BAD_CREDENTIALS = -1
  ERR_USER_EXISTS = -2
  ERR_BAD_USERNAME = -3
  ERR_BAD_PASSWORD = -4
  MAX_USERNAME_LENGTH = 128
  MAX_PASSWORD_LENGTH = 128

  test "user should have non-empty user name" do
    User.TESTAPI_resetFixture
    errCode = User.add("", "adf")
    assert(errCode == ERR_BAD_USERNAME, "Empty username should be bad")
  end

  test "username with MAX_USERNAME_LENGTH should succeed" do
    User.TESTAPI_resetFixture
    s = ""
    for i in 1..MAX_USERNAME_LENGTH
      s << "a"
    end
    errCode = User.add(s, "sbdf344")
    assert(errCode == SUCCESS, "128 is a valid username length")
  end

  test "password that is an empty string should succeed" do
    User.TESTAPI_resetFixture
    errCode = User.add("Bob", "")
    assert(errCode == SUCCESS, "empty string is a valid password")
  end

  test "user with non-empty username and password should succeed"
    User.TestAPI_resetFixture
    errCode = User.add("kittens", "mittens")
    assert(errCode == SUCCESS, "standard username and password suceeds")
  end

end
