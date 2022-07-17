/**
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import java.io.IOException;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.util.GenericOptionsParser;

public class Part {

  public static class TokenizerMapper 
       extends Mapper<Object, Text, Text, IntWritable>{
    
    private final static IntWritable one = new IntWritable(1);
    private Text word = new Text();
      
    public void map(Object key, Text value, Context context
                    ) throws IOException, InterruptedException {
    	
    	
			word.set(value.toString().split(",")[2]);
	    	context.write(word, one);
		
       
    }
  }
  

  public static class IntSumReducer 
       extends Reducer<Text,IntWritable,Text,IntWritable> {
    private IntWritable result = new IntWritable();

    public void reduce(Text key, Iterable<IntWritable> values, 
                       Context context
                       ) throws IOException, InterruptedException {
    //此时传进来的value是一个值的集合 <hello,[1,1,1]>
      int sum = 0;
      for (IntWritable val : values) {
        sum += val.get();//用for循环将value值累加
      }
      result.set(sum);//把sum值赋给result
      context.write(key, result);//输出<hello,3>
    }
  }

  public static void main(String[] args) throws Exception {
    Configuration conf = new Configuration();//配置对象conf,可以配置mapreduce的参数，不过这里没有配置别的
    String[] otherArgs = new GenericOptionsParser(conf, args).getRemainingArgs();
    if (otherArgs.length < 2) {
      System.err.println("Usage: wordcount <in> [<in>...] <out>");
      System.exit(2);
    }
    Job job = Job.getInstance(conf, "word count"); //新建一个job 用于控制工作流程
    job.setJarByClass(Part.class); //设置工作类名 Part
    job.setMapperClass(TokenizerMapper.class);//设置mapper的类 TokenizerMapper.class
    job.setCombinerClass(IntSumReducer.class);//设置combiner的类 IntSumReducer.class
    job.setReducerClass(IntSumReducer.class);//设置reducer的类 IntSumReducer.class
    job.setOutputKeyClass(Text.class);//设置输出key的类型 text 
    job.setOutputValueClass(IntWritable.class);//设置输出value的格式 int类型  输出整体是这样的： hello 2
    for (int i = 0; i < otherArgs.length - 1; ++i) {
      FileInputFormat.addInputPath(job, new Path(otherArgs[i])); //设置输入路径
    }
    FileOutputFormat.setOutputPath(job,
      new Path(otherArgs[otherArgs.length - 1]));//设置输出路径
    System.exit(job.waitForCompletion(true) ? 0 : 1);
  }
}

