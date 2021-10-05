require 'spec_helper'

describe package('nginx'), :if => os[:family] == 'ubuntu' do
  it { should be_installed }
end

describe package('php'), :if => os[:family] == 'ubuntu' do
  it { should be_installed }
end

describe package('postgres'), :if => os[:family] == 'ubuntu' do
    it { should be_installed }
  end


describe service('nginx'), :if => os[:family] == 'redhat' do
  it { should be_enabled }
  it { should be_running }
end

describe service('postgres'), :if => os[:family] == 'ubuntu' do
  it { should be_enabled }
  it { should be_running }
end

describe port(80) do
  it { should be_listening }
end

describe file('/etc/nginx/nginx.conf') do
    it { should be_file }
end

describe file('/etc/nginx/sites-available') do
    it { should be_directory }
end

describe file('/etc/nginx/sites-enabled') do                                                                                                                                                                   it { should be_directory }
end

describe file('/etc/php/7.0/fpm/php.ini') do                                                                                                                                                                   it { should be_directory }
end

describe file('/var/lib/pgsql/data/postgresql.conf') do                                                                                                                                                                   it { should be_directory }
end


