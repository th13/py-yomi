# encoding: utf-8

require 'bunny'
require 'json'
require './parser'

connection = Bunny.new host: "rabbit-server"
connection.start

channel = connection.create_channel

class ParserServer
  def initialize(channel)
    @channel = channel
  end

  def start(queue_name)
    @queue = @channel.queue(queue_name)
    @exchange = @channel.default_exchange

    @queue.subscribe(block: true) do |delivery_info, properties, body|
      text = body.force_encoding('utf-8')
      words = parse_jp(text).to_json      
      @exchange.publish(words,
                        routing_key: properties.reply_to,
                        correlation_id: properties.correlation_id)
    end
  end
end

begin
  server = ParserServer.new(channel)
  puts "[jp_parser] Waiting for requests."
  server.start "rpc_queue"
rescue Interrupt => _
  channel.close
  connection.close
end

