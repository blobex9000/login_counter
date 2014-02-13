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

  test "username with MAX_USERNAME_LENGTH should be added" do
    User.TESTAPI_resetFixture
    s = ""
    for i in 1..MAX_USERNAME_LENGTH
      s << "a"
    end
    errCode = User.add(s, "sbdf344")
    assert(errCode == SUCCESS, "128 is a valid username length")
  end

  test "password that is an empty string should be added" do
    User.TESTAPI_resetFixture
    errCode = User.add("Bob", "")
    assert(errCode == SUCCESS, "empty string is a valid password")
  end

  test "user with not empty username and password should be added" do
    User.TESTAPI_resetFixture
    errCode = User.add("kittens", "mittens")
    assert(errCode == SUCCESS, "standard username and password suceeds")
  end

  test "password with MAX_PASSWORD_LENGTH should be added" do
    User.TESTAPI_resetFixture
    s = ""
    for i in 1..MAX_PASSWORD_LENGTH
      s << "a"
    end
    errCode = User.add("blah", s)
    assert(errCode = SUCCESS, "password with max length should be added")
  end

  test "user with username larger than max should not be added" do
    User.TESTAPI_resetFixture
    s_len = MAX_USERNAME_LENGTH + 1
    for i in 1..s_len
      s << "b"
    end
    errCode = User.add("fred", s)
    assert(errCode = SUCCESS, "username that is too long shouldn't be added")
  end

  test "added user should be able to login and count should be 1" do
    User.TESTAPI_resetFixture
    errCodeAdd = User.add("ted", "web")
    errCodeLogin = User.login("ted", "web")
    assert(errCodeAdd = SUCESS && errCodeLogin = 1, "added user should be able to login")
  end

end
